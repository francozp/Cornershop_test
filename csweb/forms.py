from django import forms
from .models import *
from django.contrib.auth.models import User
import datetime

class MenuForm(forms.Form):
    # Form for menu creation
    maindish = forms.CharField(label = "Plato Principal", widget=forms.Select(attrs={'required': True}))
    salad = forms.BooleanField(label = "Ensalada", widget=forms.CheckboxInput(), initial=True, required=False)
    dessert = forms.BooleanField(label = "Postre", widget=forms.CheckboxInput(), initial=True, required=False)

class EditMenuForm(forms.Form):
    maindish = forms.CharField(label = "Plato Principal", widget=forms.Select(attrs={'required': True}))
    salad = forms.BooleanField(label = "Ensalada", widget=forms.CheckboxInput(), initial=True, required=False)
    dessert = forms.BooleanField(label = "Postre", widget=forms.CheckboxInput(), initial=True, required=False)

class ModalForm(forms.Form):
    # Form for dish creation
    newdish = forms.CharField(label = "Plato Principal", widget=forms.TextInput())    
    
class OptionForm(forms.Form):
    option = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), choices=[])
    detail = forms.CharField(widget=forms.Textarea,required=False)

class UserRegistrationForm(forms.Form):
    name = forms.CharField(required=True,label='Nombre',max_length=32)
    privilege = forms.BooleanField(widget = forms.CheckboxInput(), initial=True, required=False)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password','name','rut','privilege')
        
MenuFormSet = forms.formset_factory(MenuForm, can_delete=True)
ModalFormSet = forms.formset_factory(ModalForm, can_delete=True)
EditFormSet = forms.formset_factory(EditMenuForm, can_delete=True)