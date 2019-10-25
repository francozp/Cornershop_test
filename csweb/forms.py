from django import forms
from .models import *

class MenuForm(forms.Form):
    date = forms.DateTimeField(label="Fecha", input_formats=['%d/%m/%Y', '%d/%m/%y'], widget=forms.DateTimeInput(format = '%d/%m/%Y', attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}))
    maindish = forms.CharField(label = "Plato Principal", widget=forms.TextInput())
    salad = forms.BooleanField(label = "Ensalada", widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}), required=False)
    dessert = forms.BooleanField(label = "Postre", widget=forms.CheckboxInput(attrs={'class': 'custom-control-input'}), required=False)
    
    

MenuFormSet = forms.formset_factory(MenuForm, can_delete=True)