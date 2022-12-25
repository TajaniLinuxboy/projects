from django.urls import path
from feedbackapp.views import home, success

urlpatterns = [
    path('', home, name="feedback-home"),
    path('success/', success, name="feedback-success")
]
