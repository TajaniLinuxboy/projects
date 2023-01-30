import secrets

from django import forms
from django.core.validators import validate_email, validate_slug
from django.core.exceptions import ValidationError
from login.models import Register
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_api_key.models import APIKey

#Custom Validators


#My Forms
class RegisterForm(forms.Form): 
        email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True, validators=[validate_email])
        password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True, validators=[validate_slug])

        def clean(self):
                cleaned_data = super().clean()
                _email = cleaned_data.get('email')
                _password = cleaned_data.get('password')

                if _email and _password:
                       passwd =  make_password(_password, salt=secrets.token_hex(32))
                       apikey, key = APIKey.objects.create_key(name=f'{_email} key')
                       
                       user = Register(
                        email=_email,
                        password=passwd,
                        api_token = key,
                       ).save()
                
                else: 
                        raise ValidationError("Bad Email or Password")


class LoginForm(forms.Form): 
        email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True, validators=[validate_email])
        password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), required=True, validators=[validate_slug])

      


class ForgotPasswordForm(forms.Form): 

        email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True, validators=[validate_email])


        def clean_email(self):
                data = self.cleaned_data['email']

                try:
                        check_email = Register.objects.get(email=data)
                        passwd = ''
                except Register.DoesNotExist:
                        raise ValidationError("User doesn't exist")



