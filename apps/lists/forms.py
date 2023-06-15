from django.forms import ModelForm
from .models import Category, Item

from django import forms



class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'





# class ItemForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = '__all__'


class ItemForm(forms.Form):

    item = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    
    