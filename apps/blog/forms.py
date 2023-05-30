from django.forms import ModelForm
from .models import Book, Author, Article,  Comment #User,

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from django.forms.widgets import PasswordInput, TextInput


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'




class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"




# usign Django's user model and authentication


# Register/Create user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Login a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())