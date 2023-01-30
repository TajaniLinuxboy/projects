from django.urls import path
from login import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
]