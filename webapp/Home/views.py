from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from Post.models import Post
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from itertools import chain

# Create your views here.
def Home(request):
    Posts = Post.objects.all().order_by('time')
    data = {'Posts': Posts}
    
    if request.user.is_authenticated:
        user = request.user
        liked = Post.objects.filter(is_liked=user).order_by('time')
        not_liked = Post.objects.exclude(is_liked=user).order_by('time')
        data['Liked'] = liked
        data['Not_Liked'] = not_liked
    return render(request, 'home.html', data)

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
    return redirect('Home')

def Logout(request):
    logout(request)
    return redirect('Home')

def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = authenticate(request, username=username, password=password)
        if not user:
            new_user = User.objects.create(username=username, password=password, email=email)
            new_user.save()
            login(request, new_user)
    return redirect('Home')

def Profile(request):
    if request.user.is_authenticated:
        user = request.user
        liked = Post.objects.filter(is_liked=user)
        return render(request, 'profile.html', {'Liked': liked})
    else:
        return redirect('Home')