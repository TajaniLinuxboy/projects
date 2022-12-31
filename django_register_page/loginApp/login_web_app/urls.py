from django.urls import path
from login_web_app.views import home

urlpatterns = [
    path('', home, name='register-home'),
]