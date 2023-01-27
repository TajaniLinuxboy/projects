from rest_framework import serializers
from login.models import Movie

class MovieSerialzer(serializers.ModelSerializer):
    class Meta: 
        model = Movie
        fields = '__all__'