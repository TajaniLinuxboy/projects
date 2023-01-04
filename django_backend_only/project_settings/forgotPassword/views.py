import secrets

from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from forgotPassword.forms import RecoveryForm, SetPasswordForm
from project_settings.settings import SUCCESS, EMAIL_HOST_USER
from authorization.models import registerModel, TemporaryTokenModel
from project_settings import logger
from project_settings.settings import SECRET_KEY
from django.contrib.auth.hashers import make_password
from django.contrib import messages

REGISTER_QUERY = registerModel.objects
TEMPKEY_QUERY = TemporaryTokenModel.objects

# Create your views here.

def recover(request):

    if request.method == "POST":
        form = RecoveryForm(request.POST)
        email = request.POST.get('email')

        try: 
            user = REGISTER_QUERY.get(email=email)
            try:
                check_user = TEMPKEY_QUERY.get(registermodel__email__contains=user.email)
            except TemporaryTokenModel.DoesNotExist: 
                token_creation = TemporaryTokenModel(token=secrets.token_urlsafe(32), registermodel=user).save()
                temp_token = TEMPKEY_QUERY.get(registermodel__email__contains=email).token
                message = f"RESET PASSWORD URL: 'http://127.0.0.1:8000/forgotpassword/forgot_password_activation/?temp_token={temp_token}"

                send_mail(
                    subject="Recover Password",
                    from_email=EMAIL_HOST_USER,
                    message=message, 
                    recipient_list=[email]
                )

                messages.success(request, f"Email sent to: {email}")
                return HttpResponse(SUCCESS)
        except registerModel.DoesNotExist:
            messages.error(request, f"Invalid Email: {email}")

    form = RecoveryForm()
    return render(request, 'forgotPassword/recovery.html', context={'form': form})



def recover_link(request):
    form = SetPasswordForm()

    if request.method == "GET":
        temporary_token = request.GET['temp_token']

        try:
            check_temp_token = TEMPKEY_QUERY.get(token=temporary_token)
        except TemporaryTokenModel.DoesNotExist: 
            messages.error(request, "Invalid Token")
    
    if request.method == 'POST':
        form = SetPasswordForm(request.POST)
        if form.is_valid(): 
            try: 
                temporary_token = request.GET['temp_token']
                temp_token = TEMPKEY_QUERY.get(token=temporary_token)
                
                new_paswd = make_password(form.cleaned_data.get('password'), salt=secrets.token_hex(32))
                query = REGISTER_QUERY.filter(email=temp_token.registermodel.email).first()

                query.password = new_paswd
                query.save()
                logger.debug(query)
                temp_token.delete()
                
                messages.success(request, "Password Changed")
                return redirect(reverse('auth-login'))

            except TemporaryTokenModel.DoesNotExist:
                messages.info(request, "Need Email")
                return redirect(reverse('forgotpassword-home'))

    return render(request, 'forgotPassword/recover_link.html', context={'form': form})
