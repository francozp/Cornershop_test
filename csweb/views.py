from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import *
import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

class MenuView(FormView):
    form_class = MenuForm
    template_name = "menu.html"

    def get_context_data(self, **kwargs):
        data = super(MenuView, self).get_context_data(**kwargs)
        if self.request.POST:
            form = MenuForm(self.request.POST or None)
            data["form"] = form
            if form.is_valid():
                print(form.cleaned_data['maindish'])
                """pedido = Pedido.objects.create(obra=Obra.objects.get(id=obra),
                                               usuario=self.request.user,
                                               fecha=timezone.now(),
                                               comentario=comentario)"""
            else:
                print(form.errors) #doesn't print anything
                print(form.non_field_errors()) #doesn't print anything
                print('Errors')
        else:
            form = MenuForm()   
            data["form"] = form
            print("la concha del mono")
        data["date"] = datetime.datetime.now()
        return data

    def render_to_response(self, context):
        return super(MenuView, self).render_to_response(context)
    
    def form_valid(self, form):
        context = self.get_context_data()
        print(context)
        return super(MenuView, self).form_valid(form)
    