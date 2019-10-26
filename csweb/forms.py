from django import forms
from .models import *

class MenuForm(forms.Form):
    maindish = forms.CharField(label = "Plato Principal", widget=forms.TextInput())
    salad = forms.BooleanField(label = "Ensalada", widget=forms.CheckboxInput(), initial=False, required=False)
    dessert = forms.BooleanField(label = "Postre", widget=forms.CheckboxInput(), initial=False, required=False)
    
    

MenuFormSet = forms.formset_factory(MenuForm, can_delete=True)