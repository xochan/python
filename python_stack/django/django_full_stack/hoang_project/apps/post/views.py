from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from apps.login.models import User

def post(request):
    userx = User.objects.get(id=request.session['idnumber'])
    postx = Post.objects.exclude(user_fav_post = userx)
    context = {
        'first_name' : userx.first_name,
        'idnumber' : request.session['idnumber'],
        'posts': Post.objects.all().order_by('-created_at'),
        'admin': userx.admin,
        'post_not_favorite': postx
    }
    return render(request, 'post/post.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def post_post(request):
    if request.method == 'POST':
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/post')
        else:   
            post = request.POST['post']
            iduser = request.POST['iduser']
            userx = User.objects.get(id=iduser)
            Post.objects.create(user=userx, post=post)
            return redirect('/post')

def add_favorite(request):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    userx = User.objects.get(id=request.session['idnumber'])
    userx.fav_post.add(postx)
    return redirect('/post')

def user_favorite(request, number):
    userx = User.objects.get(id=number)
    context = {
        'first_name' : userx.first_name,
        'idnumber' : request.session['idnumber'],
        'user_favorite': userx.fav_post.all().order_by('-created_at')
    }
    return render(request, 'post/favorite.html', context)

def remove_favorite(request, number):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    userx = User.objects.get(id=number)
    userx.fav_post.remove(postx)
    return redirect('/post/'+number+'/favorite')

def remove_post(request):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    postx.delete()
    return redirect('/post')

def editsubmit(request, number):
    if request.method == 'POST':
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            print('you have error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/post')
        else:   
            idnumber = number
            post = request.POST['post']
            postx = Post.objects.get(id=idnumber)
            postx.post = post
            postx.save()
            return redirect('/post')
    else:
        return redirect('/post')

