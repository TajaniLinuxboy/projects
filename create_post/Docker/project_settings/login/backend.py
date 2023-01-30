from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.sessions.models import Session

from login.models import Register
from project_settings.settings import logger


class AuthenticateUser(BaseBackend):
    ip = None
    pk = None

    def get_user(self, pk):
        try: 
            user = Register.objects.get(pk=pk)
            return user
        except Register.DoesNotExist: 
            return None
    
    def client_ip(self, request): 
        headers = request.META
        x_forwarded = headers.get('HTTP_X_FORWARDED_FOR')
        remote_addr = headers.get('REMOTE_ADDR')
        current_ip = x_forwarded or remote_addr

        self.ip = current_ip

        return True


    def login(self, request, pk, password):
        user = self.get_user(pk)
        self.client_ip(request)

        if user: 
            _passwd = user.password
            if check_password(password, _passwd):
                request.session.expire_date = 0
                request.session['user_email'] = user.email
                request.session['ip_addr'] = self.ip
                return True
            else: 
                return False

    
    def session_login(self, request):
        session_ip_addr = request.session.get('ip_addr')
        self.client_ip(request)

        try: 
            s = Session.objects.get(pk=request.COOKIES.get('sessionid'))

            if session_ip_addr == self.ip:
                return True
            else: 
                return False
        
        except Session.DoesNotExist: 
            return None
         

    def logout(self, request):
        request.session.flush()
        return True    


    def is_authenticated(self, redirect_true=None, redirect_false=None):
        def wrapfunc(func): 
            def inner_wrap(request):

                if self.session_login(request):
                    if redirect_true: 
                        return redirect(reverse(redirect_true))    
                    else: 
                        return func(request)

                else:
                    if redirect_false:  
                        return redirect(reverse(redirect_false))
                    else: 
                        return func(request)
            return inner_wrap
        return wrapfunc
