import secrets

from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from forgotPassword.forms import RecoveryForm, SetPasswordForm
from project_settings.settings import SUCCESS, EMAIL_HOST_USER
from authorization.models import registerModel, TemporaryTokenModel
from project_settings.settings import SECRET_KEY
from django.contrib.auth.hashers import make_password
from project_settings import logger

REGISTER_QUERY = registerModel.objects
TEMPKEY_QUERY = TemporaryTokenModel.objects

# Create your views here.

def recover(request):

    if request.method == "POST":
        form = RecoveryForm(request.POST)
        email = request.POST.get('email')

        logger.info(reverse('recover-password'))
        try: 
            user = REGISTER_QUERY.get(email=email)
            try:
                check_user = TEMPKEY_QUERY.get(registermodel__email__contains=user.email)
            except TemporaryTokenModel.DoesNotExist: 
                token_creation = TemporaryTokenModel(token=secrets.token_urlsafe(32), registermodel=user).save()
                temp_token = TEMPKEY_QUERY.get(registermodel__email__contains=email).token
                message = f"RESET PASSWORD URL: {request.build_absolute_uri(reverse('recover-password'))}?temp_token={temp_token}"                

                send_mail(
                    subject="Recover Password",
                    from_email=EMAIL_HOST_USER,
                    message=message, 
                    recipient_list=[email]
                )

                return HttpResponse(SUCCESS)
        except registerModel.DoesNotExist: 
            print("Can't find Account")

    form = RecoveryForm()
    return render(request, 'forgotPassword/recovery.html', context={'form': form})



def recover_link(request):
    form = SetPasswordForm()

    if request.method == "GET":
        temporary_token = request.GET['temp_token']

        try:
            check_temp_token = TEMPKEY_QUERY.get(token=temporary_token)
        except TemporaryTokenModel.DoesNotExist: 
            logger.debug('User does not exist')

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

                return redirect(reverse('auth-login'))

            except TemporaryTokenModel.DoesNotExist:
                return redirect(reverse('forgotpassword-home'))

    return render(request, 'forgotPassword/recover_link.html', context={'form': form})