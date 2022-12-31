from django.shortcuts import render, HttpResponse
from login.forms import LoginForm
from login_web_app.models import Users
from loginApp.settings import SUCCESS
from django.contrib import messages
from loginApp import logger
# Create your views here.

def login(request): 
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            mail = form.cleaned_data.get('email')
            passwd = form.cleaned_data.get('password')


            return HttpResponse(SUCCESS)

    return render(request, "login/index.html", context={"form": form})


