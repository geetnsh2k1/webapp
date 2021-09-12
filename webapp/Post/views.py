from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from Post.models import Post
from django.contrib.auth.models import User

# Create your views here.
def Like(request, id):
    data = {'status': False}
    try:
        user = request.user
        post = Post.objects.get(id=id)
        post.is_liked.add(user)
        post.save()
        data['status'] = True
    except Exception as e:
        print(e)
    return JsonResponse(data)

def Unlike(request, id):
    data = {'status': False}
    try:
        user = request.user
        post = Post.objects.get(id=id)
        post.is_liked.remove(user)
        post.save()
        data['status'] = True
    except Exception as e:
        print(e)
    return JsonResponse(data)

def Add(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            event_name = request.POST['name']
            data = request.POST['data']
            time = request.POST['time']
            location = request.POST['location']
            image = request.FILES.get('image', False)
            
            post = Post.objects.create(created=user, event_name=event_name, data=data, time=time, location=location)
            
            if image:
                post.image = image
            
            post.save()
            
    return redirect('Home')
    