from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from feedbackapp.forms import FeedBackForm
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def home(request):
    if request.method == "POST":
        form = FeedBackForm(request.POST)

        if form.is_valid():
            send_mail(
                subject="FeedBackForm",
                message="Thank You For Completing the Form",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['email']],
            )
            return redirect('/success/')

    else:
        form = FeedBackForm() 

    return render(request, 'feedbackapp/index.html', {"form": form})



def success(request): 
    return HttpResponse("<h1>Success</h1>")
