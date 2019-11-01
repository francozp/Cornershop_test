from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, FormView, ListView, DetailView,CreateView
from django_slack import slack_message
from .tasks import slack_msg
import hashlib
from .models import *
from .forms import *
import uuid
import datetime
import socket 

# ------------ MAIN TO-DO List ----------------
# TODO: Create the main screen
# TODO: Create the user control
# TODO: Create the login view
# TODO: User select option from menu (until 11am, with customizations)
# TODO: Nora can see the options from users

class HomeView(TemplateView):
    template_name = "index.html"

# TODO: Verify if the menu is already created

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
                        msg += "Opción " + str(i+1) + ": " + maindish  
                        # Add the options to the slack msg
                        if(salad and dessert):
                            msg += ", Ensalada y Postre\n"
                        elif(salad):
                            msg += " y Ensalada\n"
                        elif(dessert):
                            msg += " y Postre\n"
                        else:
                            msg += "\n"
                        option = Options.objects.create(option_id = idoption, main_id = idmain, menu_id = idmenu, salad = salad, dessert = dessert,menu_option=i+1)
                    host_name = socket.gethostname() 
                    host_ip = socket.gethostbyname(host_name) 
                    msg += "\nTengan lindo día!\n\n El menú puede verse en http://" + str(host_ip) + ":8000/menu/" + str(idmenu)
                    #deliver = datetime.datetime(date_list[2], date_list[1], date_list[0], 9, 00)
                    today = datetime.datetime.now()
                    deliver = datetime.datetime(int(date_list[2]), int(date_list[1]), int(date_list[0]), 9)
                    cdw = (deliver-today).total_seconds()
                    if(cdw< 0):
                        cdw = 0
                    slack_msg.apply_async(kwargs={'msg': msg},countdown=int(cdw))
                    # Send the slack msg async using celery (view tasks.py and celery.py)
            else:
                print(form_data.errors)
            data['options'] = MenuFormSet()
            data['modal'] = ModalFormSet()
        else:
            data['options'] = MenuFormSet()
            data['modal'] = ModalFormSet()
        return data

    def form_valid(self, form):
        return super(MenuView, self).form_valid(form)

class MenuDetailView(DetailView):
    model = Menu
    template_name = "ver_menu.html"
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

class RegisterView(FormView):
    form_class = UserRegistrationForm
    # Main form class for the view
    template_name = 'register.html'
    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            form = UserRegistrationForm(self.request.POST)
            print(form)
            if form.is_valid():
                # Validate if the form is valid
                userid = str(uuid.uuid4())
                # Create the uuid for the user_id
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                hashed_pwd = str(hashlib.sha512(str(password).encode('utf-8')).hexdigest())
                # Hash the passwrod using hashlib
                privilege = bool(self.request.POST.get('privilege',False))
                rut = form.cleaned_data.get('rut')
                name = form.cleaned_data.get('name')
                profile = Profile.objects.create(username = username, user_id= userid,rut=rut,name=name,privileges=True, password = hashed_pwd)
                profile.save()
                # Create and save the Profile object created
            else:
                print(form.errors)
        else:
            form = UserRegistrationForm()
        context['form'] = form
        return context
    
    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

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