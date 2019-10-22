from django.shortcuts import render
from django.views.generic import TemplateView
from dal import autocomplete
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

class MenuView(TemplateView):
    template_name = "menu.html"