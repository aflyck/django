from django import forms
from .models import ProgramLanguage, City


class FinderForm(forms.Form):
    city = forms.ModelChoiceField(
        City.objects.all(), to_field_name='slug', required=False,
    widget=forms.Select(attrs={'class': "form-select"}),
    label = "Город")
    program = forms.ModelChoiceField(
        ProgramLanguage.objects.all(), to_field_name='slug', required=False,
    widget=forms.Select(attrs={'class': "form-select"}),
    label = "Специальность")