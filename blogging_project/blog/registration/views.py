from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from .models import Post
import time


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    # Retrieve individual variables from each post and store in a 2D array
    post_data = []
    for post in posts:
        post_data.append([
            post.author.username,
            post.title,
            post.description,
            post.created_at,
            post.updated_at,
        ])

    return render(request, 'main/home.html', {"posts": post_data})


@login_required
def check_login_status(request):
    # If the user is logged in, return a success message
    return render(request, 'main/home.html')



@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {"form": form})