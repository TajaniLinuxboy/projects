from django.shortcuts import render, redirect
from django.http import HttpResponse
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
                message=f"Thank you {form.cleaned_data['firstname']} {form.cleaned_data['lastname']} for responding",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[form.cleaned_data['email']],
            )
            return HttpResponse("<h1>Success</h1>")

    else:
        form = FeedBackForm() 

    return render(request, 'feedbackapp/index.html', {"form": form})
