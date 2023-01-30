from django import forms
from django.core.validators import validate_email, validate_slug
from django.core.exceptions import ValidationError
from account.models import Post
from login.views import auth
from project_settings.settings import logger

class PostForm(forms.Form):
        title = forms.CharField(widget=forms.TextInput(
                attrs={
                        'class': 'header',
                        'placeholder': 'Title'
                }
        ), max_length=30,  required=True)
        
        link = forms.CharField(widget=forms.URLInput(attrs={
                        'class': 'input-link',
                        'placeholder': "Enter Link Here",
                }
        ), max_length=200, required=True) 
        

        comment = forms.CharField(widget=forms.Textarea(
                     attrs={
                             'class': 'comment',
                             'rows': 3, 
                             'cols': 40,
                             'placeholder': "Comment about link",
                             'name': 'comment',
                             }
                     ), max_length=300, required=True)
        
