from django.urls import path
from feedbackapp.views import home

urlpatterns = [
    path('', home, name="feedback-home"),
]
