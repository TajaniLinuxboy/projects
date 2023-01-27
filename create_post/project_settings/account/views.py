from django.shortcuts import render, redirect
from django.urls import reverse

from login.views import auth
from login.models import Register

from account.forms import PostForm
from account.models import Post

from project_settings.settings import logger

# Create your views here.
@auth.is_authenticated(redirect_false='login')
def account(request): 
    return render(request, 'account/account.html')


@auth.is_authenticated(redirect_false='login')
def mypost(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            email = Register.objects.get(pk=request.session.get('user_email'))

            p = Post(
                email=email,
                title=form.cleaned_data.get('title'),
                link=form.cleaned_data.get('link'),
                comment=form.cleaned_data.get('comment')
            ).save()

            return redirect(reverse('mypost'))
    return render(request, 'account/postlinks.html', context={'form': form})