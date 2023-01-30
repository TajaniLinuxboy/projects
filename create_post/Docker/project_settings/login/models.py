from django.db import models
from rest_framework.serializers import ModelSerializer


# Create your models here.
class Register(models.Model): 
    email = models.EmailField(max_length=200, primary_key=True)
    password = models.CharField(max_length=200)
    api_token = models.CharField(max_length=50)


class RegisterSerializer(ModelSerializer):
 
    class Meta:
        model = Register
        fields = ['email', 'api_token']

