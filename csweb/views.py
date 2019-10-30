from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, FormView, ListView, DetailView
from django_slack import slack_message
from .tasks import slack_msg
from .models import *
from .forms import *
import uuid
import datetime
# ------------ MAIN TO-DO List ----------------
# TODO: Create the main screen
# TODO: Create the user control
# TODO: Add option number field to option model
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
                date = str(self.request.POST['date']).split("/")
                date = date[2] + "-" + date[1] +"-" + date[0]
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
                    msg += "\nTengan lindo día!"
                    slack_msg.delay(msg)
                    # Send the slack msg
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
        sorted_options = sorted(options, key=lambda x: x.menu_option)
        dishes = []
        for option in sorted_options:
            dish = MainDish.objects.filter(main_id = option.main_id)
            dishes.append(dish[0])
        menuDetail = zip(sorted_options,dishes)
        context['menu'] = menuDetail
        return context

    def render_to_response(self, context):
        return super(MenuDetailView, self).render_to_response(context)


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