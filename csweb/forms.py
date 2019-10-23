from django import forms
from .models import *

class MenuForm(forms.Form):
    date = forms.DateField(label="Fecha", widget=forms.SelectDateWidget())
    maindish = forms.CharField(label = "Plato Principal", widget=forms.TextInput())
    salad = forms.BooleanField(label = "Ensalada")
    dessert = forms.BooleanField(label = "Postre")
    
    

MenuFormSet = forms.formset_factory(MenuForm, can_delete=True)