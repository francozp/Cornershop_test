from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, ListView, DetailView,CreateView,DeleteView
from django.views.generic.edit import FormMixin
from django_slack import slack_message
from .tasks import slack_msg
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
import uuid
import datetime
import socket 

# ------------ MAIN TO-DO List ----------------
# TODO: Nora can edit the menu (before 9am of the day)

def parse_food(option, number, maindish, show_option = True):
    """ Parse the option, maindish, salad and dessert

        Parameters
        ----------
        option : object, optional
            Option object
        number : int
            Number of the option in the menu
        maindish : str
            Name of the main dish
        show_option : bool, optional
            True to show the option number
    """

    if show_option:
        msg = "Opción " + str(number) + ": " + str(maindish)
    else:
        msg = str(maindish)
    salad = option.salad
    dessert = option.dessert
    if(salad and dessert):
        msg += ", Ensalada y Postre\n"
    elif(salad):
        msg += " y Ensalada\n"
    elif(dessert):
        msg += " y Postre\n"
    else:
        msg += "\n"
    return msg

# NOTE: Needs discussion or investigation -@Franco at 02-11-2019 20:47:12
# The actual view will stay as it is
@method_decorator(login_required, name="dispatch")
class HomeView(TemplateView):
    template_name = "index.html"


@method_decorator(login_required, name="dispatch")
class MenuView(FormView):
    template_name = "menu.html"
    form_class = MenuForm
    # Main form class for the view
    def get_context_data(self, **kwargs):
        data = super(MenuView, self).get_context_data(**kwargs)
        # Date error does not exist
        data["date_error"] = None
        if self.request.POST:
            modal_data = ModalFormSet(self.request.POST)
            # This form is use to take data from the modal to create a new dish
            form_data = MenuFormSet(self.request.POST)
            # This form is use to take data to create the menu
            if(modal_data.is_valid()):
                # If the modal data is valid, we create the new dish
                maindish = str(self.request.POST['form-0-newdish'])
                idmain = str(uuid.uuid4())
                main_dish = MainDish.objects.create(main_id = idmain , description = maindish)
            else:
                print(modal_data.errors)
            if form_data.is_valid():
                msg = "Hola!\nDejo el menú de hoy :)\n\n"
                # Msg to send to slack
                date_list = str(self.request.POST['date']).split("/")
                date = date_list[2] + "-" + date_list[1] +"-" + date_list[0]
                # The date is parsed to be compatible with the MySql schema
                date_verify = Menu.objects.filter(fecha = date)
                # Verify if there is a menu created for the date 
                if(date_verify):
                    data["date_error"] = True
                else:
                    data["date_error"] = False
                    # If the main form data is vald, then the menu, dish, and options are created
                    maxforms = int(self.request.POST['form-TOTAL_FORMS'])
                    idmenu = str(uuid.uuid4())
                    menu = Menu.objects.create(menu_id = idmenu, fecha = date)
                    # TODO: Fix options not created
                    for i in range(maxforms):
                        # Iterate over the different options and create them
                        maindish = str(self.request.POST['form-{0}-maindish'.format(i)])
                        actual_dishes = MainDish.objects.filter(description = maindish)
                        idmain = actual_dishes[0].main_id
                        idoption = str(uuid.uuid4())
                        salad = bool(self.request.POST.get('form-{0}-salad'.format(i),False))
                        dessert = bool(self.request.POST.get('form-{0}-dessert'.format(i),False))
                        option = Options.objects.create(option_id = idoption, main_id = idmain, menu_id = idmenu, salad = salad, dessert = dessert,menu_option=i+1)
                        msg += parse_food(option, i+1, maindish)

                    host_name = socket.gethostname() 
                    host_ip = socket.gethostbyname(host_name) 
                    msg += "\nTengan lindo día!\n\n El menú puede verse en http://" + str(host_ip) + ":8000/menu/" + str(idmenu)
                    today = datetime.datetime.now()
                    deliver = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]), 9)
                    cdw = (deliver-today).total_seconds()
                    print("Son " + str(cdw/3600) + " horas")
                    if(cdw< 0):
                        cdw = 0
                    slack_msg.apply_async(kwargs={'msg': msg},countdown=int(cdw))
                    # Send the slack msg async using celery (view tasks.py and celery.py). The msg will be send at the 9:00 am of the day asigned to the menu
            else:
                print(form_data.errors)
            data['options'] = MenuFormSet()
            data['modal'] = ModalFormSet()
        else:
            data['options'] = MenuFormSet()
            data['modal'] = ModalFormSet()
        return data
        
    def render_to_response(self, context):
        if (self.request.user.profile.privileges == False):
            # Validate if the user has the privileges
            return redirect('Home')
        return super(MenuView, self).render_to_response(context)

    def form_valid(self, form):
        return super(MenuView, self).form_valid(form)

@method_decorator(login_required, name="dispatch")
class AddOptionsView(FormView):
    form_class = MenuForm
    template_name = "addOptions.html"
    def get_context_data(self, **kwargs):
        context = super(AddOptionsView, self).get_context_data(**kwargs)
        if self.request.POST:
            req = self.request.POST
            if "addOption" in req:
                self.request.session["menuid"] = req["addOption"]
            else:
                formset = MenuFormSet(req)
                if formset.is_valid():
                    maxforms = int(self.request.POST['form-TOTAL_FORMS'])
                    idmenu = str(self.request.session['menuid'])
                    actual_options = Options.objects.filter(menu_id = idmenu)
                    max_opt = max(actual_options, key=lambda x: x.menu_option)
                    last = max_opt.menu_option
                    cont = 1
                    for i in range(maxforms):
                        # Iterate over the different options and create them
                        maindish = str(self.request.POST['form-{0}-maindish'.format(i)])
                        actual_dishes = MainDish.objects.get(description = maindish)
                        idmain = actual_dishes.main_id
                        idoption = str(uuid.uuid4())
                        salad = bool(self.request.POST.get('form-{0}-salad'.format(i),False))
                        dessert = bool(self.request.POST.get('form-{0}-dessert'.format(i),False))
                        option = Options.objects.create(option_id = idoption, main_id = idmain, menu_id = idmenu, salad = salad, dessert = dessert,menu_option=last + cont)
                        cont += 1
                else:
                    print(formset.errors)

        menuid = self.request.session['menuid']
        options = Options.objects.filter(menu_id = menuid)
        # Search the options for the menu with menu_id
        opts = []
        options = sorted(options, key=lambda x: x.menu_option)
        # Sort the options based on the menu_option number
        for option in options:
            dish = MainDish.objects.get(main_id = option.main_id).description
            # Look for the maindish of the option
            opt = parse_food(option, option.menu_option, dish)
            # Parse the food
            opts.append(opt)
        context["menu"] = zip(opts,options)
        context["options"] = MenuFormSet()
        return context

    def render_to_response(self, context):
        if (self.request.user.profile.privileges == False):
            # Validate if the user has the privileges
            return redirect('Home')
        return super(AddOptionsView, self).render_to_response(context)

    def form_valid(self, form):
        return super(AddOptionsView, self).form_valid(form)

@method_decorator(login_required, name="dispatch")
class MenuEditView(FormMixin, DetailView):
    model = Menu
    template_name = "menuEdit.html"
    form_class = MenuForm
    def get_context_data(self, **kwargs):
        context = super(MenuEditView, self).get_context_data(**kwargs)
        if self.request.POST:
            form = self.get_form()
            req = self.request.POST
            qty = len(req)
            for i in range(1,qty):
                opt = "button_" + str(i)
                if opt in req:
                    option_id = self.request.POST["option_"+str(i)]
                    break
        
            if not form.is_valid():
                option = Options.objects.get(option_id = option_id)
                main = MainDish.objects.get(main_id = option.main_id)
                context["main"] = main.description
                context["dessert"] = option.dessert
                context["option"] = option_id
                if( option.salad ):
                    context["salad"] = "checked"
                if( option.dessert ):
                    context["dessert"] = "checked"
                context["successful_submit"] = True
            else:
                option = Options.objects.get(option_id = self.request.POST["option_id"])
                option.main_id = MainDish.objects.get(description = self.request.POST["maindish"]).main_id
                option.salad= bool(self.request.POST.get("salad",False))
                option.dessert = bool(self.request.POST.get("dessert",False))
                option.save()
                context["successful_submit"] = False
        
        options = Options.objects.filter(menu_id = context["object"].menu_id)
        # Search the options for the menu with menu_id
        opts = []
        options = sorted(options, key=lambda x: x.menu_option)
        # Sort the options based on the menu_option number
        for option in options:
            dish = MainDish.objects.get(main_id = option.main_id).description
            # Look for the maindish of the option
            opt = parse_food(option, option.menu_option, dish)
            # Parse the food
            opts.append(opt)
        context["menu"] = zip(opts,options)
        # Create a zip with opts and options list to iterate over both in the template
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form)) 

    def render_to_response(self, context):
        if (self.request.user.profile.privileges == False):
            # Validate if the user has the privileges
            return redirect('Home')
        return super(MenuEditView, self).render_to_response(context)

class MenuDetailView(DetailView):
    model = Menu
    template_name = "menu_detail.html"
    def get_context_data(self, **kwargs):
        context = super(MenuDetailView, self).get_context_data(**kwargs)
        options = Options.objects.filter(menu_id=context['object'].menu_id)
        # Search for the menu with menu_id obtained from get
        sorted_options = sorted(options, key=lambda x: x.menu_option)
        dishes = []
        # Obtain all the dishes on the menu
        for option in sorted_options:
            dish = MainDish.objects.filter(main_id = option.main_id)
            dishes.append(dish[0])
        menuDetail = zip(sorted_options,dishes)
        # Double list (zip) to iterate over them at the same time (options and dishes)
        context['menu'] = menuDetail
        return context

    def render_to_response(self, context):
        return super(MenuDetailView, self).render_to_response(context)
# TODOC
@method_decorator(login_required, name="dispatch")
class SeeOptionsView(TemplateView):
    model = UserOption
    template_name = "seeOptions.html"
    def get_context_data(self, **kwargs):
        context = super(SeeOptionsView, self).get_context_data(**kwargs)
        user_options = UserOption.objects.all()
        # Collect all the user_option objects
        options = []
        menus = []
        profiles = []
        dishes = []
        details = []
        for u_option in user_options:
            # Search for all the information to show (option, profile, menu, dish, detail)
            option = Options.objects.filter(option_id = u_option.option_id)[0]
            menu = Menu.objects.filter(menu_id = option.menu_id)[0]
            profile = Profile.objects.filter(user_id = u_option.user_id)[0]
            dish = MainDish.objects.filter(main_id = option.main_id)[0]
            detail = u_option.detail
            details.append(detail)
            options.append(option)
            menus.append(menu)
            profiles.append(profile)
            dishes.append(dish)
        useroption_data = zip(menus,options,profiles,dishes,details)
        # Create a zip with the 5 lists (menus, options, profiles, dishes, details)
        context["useroption"] = useroption_data
        return context

    def render_to_response(self, context):
        if (self.request.user.profile.privileges == False):
            # Validate if the user has the privileges
            return redirect('Home')
        return super(SeeOptionsView, self).render_to_response(context)

@method_decorator(login_required, name="dispatch")
class OptionDeleteView(DeleteView):
    # View to delete an option of the menu
    model = Options
    template_name = "delete.html"
    # template to delete confirmation
    context_object_name = "option"
    def get_success_url(self):
        success_url = reverse_lazy("editMenu", kwargs={'pk': self.object.menu_id})
        if success_url:
            return success_url
        else:
            return super(OptionDeleteView, self).get_success_url()
    # where to redirect after delete the item
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        options = Options.objects.filter(menu_id = self.object.menu_id)
        cont = 1
        for option in options:
            # Change the menu_option number for the other items on the menu
            if(option.option_id != self.object.option_id):
                option.menu_option = cont
                option.save()
                cont+=1
        return super(OptionDeleteView, self).delete(request, *args, **kwargs)

@method_decorator(login_required, name="dispatch")
class MenuListView(TemplateView):
    model = Menu
    template_name = "menulist.html"
    def get_context_data(self, **kwargs):
        context = super(MenuListView, self).get_context_data(**kwargs)
        menus = Menu.objects.all()
        # Obtain all the menu objects
        menu_options = []
        for menu in menus:
            options = Options.objects.filter(menu_id = menu.menu_id)
            # Look for all the options for the menu with pk = menu_id
            opts = []
            options = sorted(options, key=lambda x: x.menu_option)
            # Sort the options by menu_option number
            for option in options:
                dish = MainDish.objects.filter(main_id = option.main_id)[0].description
                opt = parse_food(option, option.menu_option, dish)
                opts.append(opt)
                # create the parsed text
            menu_options.append(opts)
        context["menus"] = zip(menus,menu_options)
        return context

    def render_to_response(self, context):
        if (self.request.user.profile.privileges == False):
            # Validate if the user has the privileges
            return redirect('Home')
        return super(MenuListView, self).render_to_response(context)


@method_decorator(login_required, name="dispatch")
class OptionView(FormView):
    # view to select one option of the menu
    model = Menu
    form_class = OptionForm
    template_name = "option.html"
    def get_context_data(self, **kwargs):
        context = super(OptionView, self).get_context_data(**kwargs)
        userid = self.request.user.id
        # get the user id
        already_chosen = UserOption.objects.filter(user_id= userid)
        # look for already selected option for the user
        if(len(already_chosen) != 0):
            # If the user has already choose an option, then the send alert
            context["chosen"] = True
        else:
            context["chosen"] = False
        today = datetime.datetime.now()
        year, month, day = str(today).split()[0].split("-")
        limit = datetime.datetime(int(year),int(month),int(day),11)
        rest = (limit-today).total_seconds()
        # Calculate remaining time
        if rest < 0:
            context["stop"] = True
        else:
            context["stop"] = False
        try:
            date = datetime.date.today()
            menu = Menu.objects.filter(fecha = date)
            # find the todays menu
            options = Options.objects.filter(menu_id = menu[0].menu_id)
            sorted_options = sorted(options, key=lambda x: x.menu_option)
            # Obtain all the dishes on todays menu
            CHOICES = []
            # Generate the choices for the choice field 
            for option in sorted_options:
                dish = MainDish.objects.filter(main_id = option.main_id)
                food = parse_food(option, option.menu_option, str(dish[0].description))
                # Parse the food choice
                CHOICES.append((option.option_id, food))
        except:
            CHOICES = ([])

        if self.request.method == 'POST':
            #If POST
            form = OptionForm(self.request.POST)
            form.fields["option"].choices= CHOICES
            # Assign the choices to the ChoiceField
            if(form.is_valid()):
                # If the form is valid, create the UserOption object
                optionid = self.request.POST['option']
                detail = self.request.POST['detail']
                userOpt = UserOption.objects.create(user_id= userid, option_id = optionid, detail=detail)
                # return none tu redirection
                return None 
            else:
                print(form.errors)
        else:
            form = OptionForm()
            form.fields["option"].choices= CHOICES
            # The choices are updated as well
        if(form.fields["option"].choices == []):
            # Verify if the user has already chosen an option
            context["menu"] = False
        else:
            context["menu"] = True
        
        context['form'] = form
        return context

    def render_to_response(self, context):
        if context is None:
            # if option is selected redirect to home
            return HttpResponseRedirect(reverse("Home"))
        return super(OptionView, self).render_to_response(context) 

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))  

@method_decorator(login_required, name="dispatch")
class RegisterView(CreateView):
    form_class = UserCreationForm
    # Main form class for the view
    template_name = 'register.html'
    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context["error"] = None
        if self.request.method == 'POST':
            form = UserRegistrationForm(self.request.POST)
            if form.is_valid():
                # Validate if the form is valid
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                privilege = bool(self.request.POST.get('privilege',False))
                name = form.cleaned_data.get('name')
                # Collect the information
                try:
                    user = User.objects.create_user(username, '', password)
                    # Create the user
                    profile = Profile.objects.create(user_id= user.id,name=name,privileges=privilege)
                    # Create the profile
                    user.save()
                    profile.save()
                    # Save the created objects
                    context["error"] = False
                except:
                    context["error"] = True
                # Create and save the User and Profile object created
            else:
                print(form.errors)
        else:
            form = UserRegistrationForm()
        context['form'] = form
        return context

    def render_to_response(self, context):
        if (self.request.user.profile.privileges == False):
            # Validate if the user has the privileges
            return redirect('Home')
        return super(RegisterView, self).render_to_response(context)

    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

@method_decorator(login_required, name="dispatch")
class AjaxMenuView(ListView):
    # This view obtains the different dishes to use them in the select input from the menu creation form
    http_method_names = ['get', ]

    def dispatch(self, request, *args, **kwargs):
        return super(AjaxMenuView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # Obtain the items
        return MainDish.objects.all()

    def get(self, request, *args, **kwargs):
        # Return the items to the view
        queryset = self.get_queryset()
        data = [{'id': p.main_id,'description': p.description} for p in queryset]
        return JsonResponse(data, status=200, safe=False)