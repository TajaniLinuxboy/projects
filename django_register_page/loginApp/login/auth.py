#from django.contrib.auth.backends import BaseBackend
##from django.contrib.auth.hashers import check_password
#from login_web_app.models import Users
#from loginApp import logger
#
#class LoginBackend(BaseBackend):
#
#    @staticmethod
#    def authenticate(request, email_field=None, password_field=None): 
#        mail = Users.objects.get(email=email_field)
#        logger.debug(f"{mail}: {type(mail)}")
#        passwd = mail.password #already encrypted 
#        logger.debug(f"{passwd}")
#        check_passwd = check_password(password_field, passwd)
#
#        logger.info(f"mail: {mail}, password: {passwd}, check_passwd: {check_passwd} ")
#
#        if mail and check_passwd:
#            try:
#                user = Users.objects.filter(email=email).first()
#            except Users.DoesNotExist: 
#                return None
#        return user 
#
#    def get_user(self, user_id): 
#        try: 
#            return Users.objects.get(pk=user_id)
#        except Users.DoesNotExist: 
#            return None