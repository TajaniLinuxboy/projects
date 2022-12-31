from django import forms
from login_web_app.models import Users
from django.core.validators import validate_slug


#Create your models here.
class RegisterForm(forms.ModelForm):

    username = forms.CharField(label="Username", min_length=5, max_length=100, validators=[validate_slug],widget=forms.TextInput(attrs={"class": "username", "placeholder": "Username"}))
    email = forms.EmailField(label="Email", min_length=12, widget=forms.TextInput(attrs={"class": "email", "placeholder": "Email"}))
    password = forms.CharField(validators=[validate_slug], widget=forms.PasswordInput(attrs={"class": "password", "placeholder": "Password"}), max_length=50, label="Password", min_length=10)


    def clean_username(self):
        data = self.cleaned_data.get('username')

        username_query = Users.objects.filter(username=data).first()
        if username_query:
            raise forms.ValidationError(f"Username: {data} in user already", 'same-username')
        else: 
            return data

    def clean_email(self):
        data = self.cleaned_data.get("email")

        email_query = Users.objects.filter(email=data).first()
        domains = ["gmail.com", "outlook.com"]
        split_data = str(data).split("@")

        if email_query: 
            raise forms.ValidationError(f"Email: {data} in use already", "same-email")
        else:  
            for domain in domains:
                if domain in split_data[1]:
                    return data
            raise forms.ValidationError(f"Must use: {domains}", "invalid-email")   
        
    class Meta:
        model = Users
        fields = '__all__'
