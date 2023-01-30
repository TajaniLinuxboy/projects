from django.db import models
from login.models import Register
from rest_framework.serializers import ModelSerializer

# Create your models here.
class Post(models.Model):
    email = models.ForeignKey(Register, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    link = models.URLField(max_length=200)
    comment = models.CharField(max_length=300)

class PostSerializer(ModelSerializer): 

    class Meta: 
        model = Post
        fields = ['email', 'title', 'link', 'comment']