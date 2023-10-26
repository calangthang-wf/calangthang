from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user_manage.forms import registerForm

def register(request):

    if request.method == "POST":
        rgCustomForm = registerForm(request.POST)

        if rgCustomForm.is_valid():
            rgCustomForm.save()
            messages.success(request, "Welcome to CaLangThang! Please Login!")
            return redirect('/user/login')
    else:
        rgCustomForm = registerForm()

    context = {'customRgForm': rgCustomForm}

    return render(request, 'register.html', context)

def user_login(request):

    if request.method == "POST":

        username = request.POST["login_username"]
        password = request.POST["login_password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}!')
            return redirect('/')
        else:
            messages.info(request, f'Account do not exit plz sign in')
    
    lgForm = AuthenticationForm()

    return render(request, 'login.html', {'lgForm': lgForm})

def user_logout(request):
    logout(request)
    return redirect('/user/login')

def userIndex(request):
    return render(request, 'login.html')