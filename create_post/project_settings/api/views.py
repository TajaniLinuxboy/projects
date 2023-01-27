from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import redirect
from django.urls import reverse
from project_settings.settings import logger

from account.models import Post, PostSerializer

from login.views import auth


OPTIONS = {
    '?email': 'email param',
    '?title': 'title param',
    '?link': 'link param',
    '?comment': 'comment param',
    '?help': 'help param',
    '?mode': 'all or single (default=single)',
    'help': 'Use these to query data (api/getpost/?title=blank)'
}


@api_view(['GET'])
@auth.is_authenticated(redirect_false='login')
def getpost(request):
    title = request.GET.get('title', None)
    email = request.GET.get('email', None) 
    link = request.GET.get('link', None)
    comment = request.GET.get('comment', None)
    help = request.GET.get('help', None)

    if title: 
        q = Post.objects.filter(title=title).first()
        return Response(PostSerializer(q).data)

    return Response(OPTIONS)


    

    