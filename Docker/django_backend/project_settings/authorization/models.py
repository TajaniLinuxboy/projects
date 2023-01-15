from django.db import models

# Create your models here.

class registerModel(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=50)


    class Meta: 
        db_table = "AppUsers"


class TemporaryTokenModel(models.Model): 
    token = models.CharField(max_length=150, unique=True)
    #expiration = models.DurationField()
    registermodel = models.ForeignKey(registerModel, on_delete=models.CASCADE)

    class Meta: 
        db_table = "TemporaryToken"