from django.urls import path
from account import views

urlpatterns = [
    path('mypost/', views.mypost, name='mypost')
]