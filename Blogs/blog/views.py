from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, AboutUs
import logging
from django.http import Http404 
from django.core.paginator import Paginator
from blog.forms import ContactForm,LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout




# Create your views here.


# Static demo data 
# posts = [
    #     {'id':1, 'title': 'Post 1', 'content': 'Content of Post 1'},
    #     {'id':2, 'title': 'Post 2', 'content': 'Content of Post 2'},
    #     {'id':3, 'title': 'Post 3', 'content': 'Content of Post 3'},
    #     {'id':4, 'title': 'Post 4', 'content': 'Content of Post 4'}

    # ]


def index(request):
    blog_title = "Latest Posts"

    #getting post data by url
    all_posts = Post.objects.all()

    # Paginator
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 

    return render(request,"blog1/index.html", {'blog_title': blog_title,'page_obj': page_obj})

def detail(request, slug):
    # static data
    # post  next((item for item in posts f item['id] == int(post_id)),None)

    try:
        # getting data from model by post id 
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
    
    # logger = logging.getLogger("Testing")
    # logger.debug(f'post variable is {post}')
    return render(request, "blog1/detail.html", {'post': post, 'related_posts':related_posts})
    



def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This the new URL")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")

        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            #send email or save in database
            success_message = 'Your Email has been sent!'
            return render(request,'blog1/contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug('Form validation failure')
        return render(request,'blog1/contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    else:
        form = ContactForm()
        return render(request, 'blog1/contact.html', {'form': form})
    
    
def about(request):
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content = "Default content goes here."
    else:
        about_content = about_content.content
    return render(request, "blog1/about.html", {'about_content':about_content})
     
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # user data created
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registeration Successfull. You can log in')
            return redirect("blog:login")
            
    return render(request, 'blog1/register.html',{'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
    #login form
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect("blog:dashboard") #redirect to dashboard
            print("Login Successful")
    return render(request, 'blog1/login.html', {'form':form})

def dashboard(request):
    blog_title = "My Posts"
    return render(request, 'blog1/dashboard.html', {'blog_title':blog_title})

def logout(request):
    auth_logout(request)
    return redirect("blog:index")