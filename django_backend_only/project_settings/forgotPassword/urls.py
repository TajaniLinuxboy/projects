from django.urls import path
from forgotPassword.views import recover, recover_link

urlpatterns = [
    path('', recover, name='forgotpassword-home'),
    path('forgot_password_activation/', recover_link, name="recover-password")
]