from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, BlogPostForm
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by("-created_at")[:6]
    return render(request, "home/index.html", {"posts": posts})

def explore(request):
    posts = BlogPost.objects.all().order_by("-created_at")
    return render(request, "home/explore.html", {"posts": posts})

def read_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.views += 1
    post.save()
    return render(request, "home/read_post.html", {"post": post})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home:index")
    else:
        form = SignUpForm()
    return render(request, "home/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home:index")
    else:
        form = AuthenticationForm()
    return render(request, "home/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home:index")

@login_required(login_url="home:signup")
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect("home:explore")
    else:
        form = BlogPostForm()
    return render(request, "home/create_post.html", {"form": form})


def about(request):
    return render(request, 'home/about.html')

def delete(request,t_id):
    item=BlogPost.objects.get(pk=t_id)
    item.delete()
    return redirect('home:explore')