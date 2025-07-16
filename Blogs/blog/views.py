from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Post

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    posts = [
        {'id':1, 'title': 'Post 1', 'Content': 'Content of Post 1'},
        {'id':2, 'title': 'Post 2', 'Content': 'Content of Post 2'},
        {'id':3, 'title': 'Post 3', 'Content': 'Content of Post 3'},
        {'id':4, 'title': 'Post 4', 'Content': 'Content of Post 4'}

    ]


    return render(request,"index.html", {'blog_title': blog_title, 'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request,"detail.html", {'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This the new URL")