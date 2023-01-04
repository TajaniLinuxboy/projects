from django import forms
from django.core.validators import validate_email

class RecoveryForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": 'email'}), max_length=100, validators=[validate_email])


class SetPasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'New password'}), max_length=50, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": 'Confirm password'}), max_length=50, min_length=8)


    def clean(self):
        cleaned_data = super(SetPasswordForm, self).clean()
        paswd1 = cleaned_data['password']
        paswd2 = cleaned_data['confirm_password']

        if paswd1 != paswd2:
            raise forms.ValidationError("Passwords do not match", "invalid password")
        
        return cleaned_data
        