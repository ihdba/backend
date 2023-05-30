from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


# main page and Login
def home(request):
    context = {
            'title': "Our recipes",
        }

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been loged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error in Login")
            return redirect('home')
    else:
        return render(request, 'recipes/recipes.html', context=context)



# logout

def logout_user(request):
    context = {
            'title': "Our recipes",
        }
    logout(request)
    messages.success(request, "You are successfully logged out!")


    return render(request, 'recipes/recipes.html', context=context)


# register new user
def register_user(request):


    return render(request, 'recipes/register_user.html')