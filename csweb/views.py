from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, FormView, ListView
from .models import *
from .forms import *
import uuid
import datetime

# ------------ MAIN TO-DO List ----------------
# TODO: Create the main screen
# TODO: Create the user control

class HomeView(TemplateView):
    template_name = "index.html"

# TODO: Verify if the menu is already created

class MenuView(FormView):
    template_name = "menu.html"
    form_class = MenuForm
    # Main form class for the view
    def get_context_data(self, **kwargs):
        data = super(MenuView, self).get_context_data(**kwargs)
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
                # If the main form data is vald, then the menu, dish, and options are created
                maxforms = int(self.request.POST['form-TOTAL_FORMS'])
                date = str(self.request.POST['date']).split("/")
                date = date[2] + "-" + date[1] +"-" + date[0]
                # The date is parsed to be compatible with the MySql schema
                idmenu = str(uuid.uuid4())
                menu = Menu.objects.create(menu_id = idmenu, fecha = date)
                for i in range(maxforms+1):
                    # Iterate over the different options and create them
                    maindish = str(self.request.POST['form-{0}-maindish'.format(i)])
                    actual_dishes = MainDish.objects.filter(description = maindish)
                    idmain = actual_dishes[0].main_id
                    idoption = str(uuid.uuid4())
                    salad = bool(self.request.POST.get('form-{0}-salad'.format(i),False))
                    dessert = bool(self.request.POST.get('form-{0}-dessert'.format(i),False))
                    option = Options.objects.create(option_id = idoption, main_id = idmain, menu_id = idmenu, salad = salad, dessert = dessert)
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