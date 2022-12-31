from django.shortcuts import redirect

# Create your views here.
def redirect_to_signup(request): 
    return redirect("register/")

def redirect_to_login(request): 
    pass