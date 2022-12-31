from django.urls import path
from redirect_page.views import redirect_to_signup

urlpatterns = [
    path('', redirect_to_signup),
]