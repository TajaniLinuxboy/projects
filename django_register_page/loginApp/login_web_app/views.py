from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from login_web_app.forms import RegisterForm
from login_web_app.models import Users
from django.contrib.auth.hashers import make_password
from loginApp.settings import SECRET_KEY


#Primative Responses 
SUCCESS = "<h1>Success</h1>"

# Create your views here.
def home(request): 
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = make_password(form.cleaned_data.get('password'), salt=SECRET_KEY)
            data = Users(
                username = form.cleaned_data.get("username"),
                email = form.cleaned_data.get("email"),
                password = password
            )
            data.save()
            return redirect(reverse('login-home'))
    return render(request, "login_web_app/index.html", context={'form': form})