
from django.forms import ModelForm
from .models import Exercise

from django import forms



class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ["exercise", "note","session", "date"]
        item = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))


        widgets = {
           'date': forms.DateInput(
               attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy', 'class': 'form-control'}
            )
        }