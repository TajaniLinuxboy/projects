from django.shortcuts import render, redirect
from django.urls import reverse

from login.forms import RegisterForm, LoginForm, ForgotPasswordForm
from login.backend import AuthenticateUser
from project_settings.settings import logger 

from django.contrib import messages

auth = AuthenticateUser()

# Create your views here.
@auth.is_authenticated(redirect_true='mypost')
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            messages.success(request, "Succesfully Registered")
            return redirect(reverse('login'))
    
    return render(request, 'login/register.html', context={'form': form})


@auth.is_authenticated(redirect_true='mypost')
def login(request): 
    form = LoginForm()

    if request.method == "POST": 
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if auth.login(request, email, password):
                messages.success(request, 'Successfully Logged In')
                return redirect(reverse('mypost'))    
    
    return render(request, 'login/login.html', context={'form': form})

        

@auth.is_authenticated(redirect_false='login')
def logout(request):
    if request.method == "GET":
        auth.logout(request)
        messages.success(request, 'Sucessfully Logged out')
        return redirect(reverse('login'))


@auth.is_authenticated(redirect_true='mypost')
def forgotpassword(request): 
    form = ForgotPasswordForm()

    if request.method == "POST": 
        form = ForgotPasswordForm(request.POST)

        if form.is_valid(): 
            return redirect(reverse('login'))
    
    return render(request, 'login/forgotpassword.html', context={'form': form})



