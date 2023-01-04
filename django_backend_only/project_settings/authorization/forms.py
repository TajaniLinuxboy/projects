from authorization.models import registerModel
from django import forms
from django.core.validators import validate_email


class RegisterForm(forms.ModelForm):

    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": 'email'}), max_length=100, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'password'}), max_length=50, min_length=8)

    class Meta:
        model = registerModel
        fields = ['email', 'password']


class LoginForm(forms.Form):
    
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": 'email'}), max_length=100, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'password'}), max_length=50, min_length=8)
    
        

