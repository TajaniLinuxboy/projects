from django.urls import path 
from api.views import getpost

urlpatterns = [
    path('getpost', getpost, name='api-post')
]