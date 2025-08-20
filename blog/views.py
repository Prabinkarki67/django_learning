from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

##dummy post
posts=[
    {  
        'author': 'Prabin K.',
        'title': 'Blog post 1',
        'content': 'First post content',
        'published_date': '17 August, 2025'
    },
    {
        'author': 'Bipin K.',
        'title': 'Blog post 2',
        'content': 'First post content',
        'published_date': '13 June, 2023'
    }
]



def home(request):
    context={
        ##'poster':posts,
        'poster':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html',{
        'title': "About"
    } )