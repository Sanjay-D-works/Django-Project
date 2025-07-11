from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"index.html")

def details(request, post_id):
    return HttpResponse(f"You are viewing post detail page/ And ID is {post_id}")

def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This the new URL")