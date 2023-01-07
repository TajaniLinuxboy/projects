from django.urls import path
from authorization.views import register, login

urlpatterns = [
    path("", register, name='auth-register'),
    path("login", login, name='auth-login'),
]