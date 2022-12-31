from django import forms
from login_web_app.models import Users
from django.core.validators import validate_slug

#Create your models here.
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", min_length=12, widget=forms.TextInput(attrs={"class": "email", "placeholder": "Email"}))
    password = forms.CharField(validators=[validate_slug], widget=forms.PasswordInput(attrs={"class": "password", "placeholder": "Password"}), max_length=50, label="Password", min_length=10)

    