from django import forms
from .models import *

class MenuForm(forms.Form):
    # Form for menu creation
    maindish = forms.CharField(label = "Plato Principal", widget=forms.Select(attrs={'required': True}))
    salad = forms.BooleanField(label = "Ensalada", widget=forms.CheckboxInput(), initial=True, required=False)
    dessert = forms.BooleanField(label = "Postre", widget=forms.CheckboxInput(), initial=True, required=False)

class ModalForm(forms.Form):
    # Form for dish creation
    newdish = forms.CharField(label = "Plato Principal", widget=forms.TextInput())
    
MenuFormSet = forms.formset_factory(MenuForm, can_delete=True)
ModalFormSet = forms.formset_factory(ModalForm, can_delete=True)