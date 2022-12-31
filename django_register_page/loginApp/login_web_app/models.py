from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
