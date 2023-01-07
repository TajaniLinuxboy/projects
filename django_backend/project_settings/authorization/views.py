import secrets

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from authorization.forms import RegisterForm, LoginForm
from project_settings.settings import SUCCESS, SECRET_KEY
from django.contrib.auth.hashers import make_password, check_password
from authorization.models import registerModel
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            paswd = make_password(form.cleaned_data.get('password'), salt=secrets.token_hex(32))
            register_user = registerModel(email=form.cleaned_data['email'], password=paswd)
            register_user.save()
            messages.success(request, f"{form.cleaned_data.get('email')} account created ")
            return redirect(reverse('auth-login'))
        else: 
            messages.error(request, f"User Login Failed") 

    form = RegisterForm()
    return render(request, 'authorization/register.html', context={'form': form})


def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid(): 

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            try:
                get_db_user = registerModel.objects.get(email=email)
                if check_password(password, get_db_user.password):  
                    messages.success(request, "Logged In") 
                    return HttpResponse(SUCCESS)
                else:
                    return redirect(reverse('auth-login'))
            except registerModel.DoesNotExist as e: 
                messages.error(request, e)
                
    
    form = LoginForm()
    return render(request, 'authorization/login.html', context={'form': form})

