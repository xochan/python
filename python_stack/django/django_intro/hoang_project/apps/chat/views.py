from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from apps.login.models import User

def post(request):
    userx = User.objects.get(id=request.session['idnumber'])
    postx = Post.objects.exclude(user_favorite = userx)
    context = {
        'first_name' : request.session['first_name'],
        'idnumber' : request.session['idnumber'],
        'posts': post.objects.all().order_by('-created_at'),
        'user_favorite': userx.favorite_post.all(),
        'post_not_favorite': postx
    }
    return render(request, 'first_app/post.html', context)

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

def user_infor(request, number):
    userx = User.objects.get(id=number)
    request.session['count'] = 0
    posts = userx.posts.all()
    for post in posts:
        request.session['count'] += 1
    context = {
        'name': userx.name,
        'posts': userx.posts.all()
    }
    return render(request, 'first_app/user_infor.html', context)

def add_favorite(request):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    userx = User.objects.get(id=request.session['idnumber'])
    userx.favorite_post.add(postx)
    return redirect('/post')

def remove_favorite(request):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    userx = User.objects.get(id=request.session['idnumber'])
    userx.favorite_post.remove(postx)
    return redirect('/post')

def remove_post(request):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    postx.delete()
    return redirect('/post')

def edit(request, number):
    context = {
        'idnumber': number
    }
    print(number)
    return render(request, 'first_app/edit.html', context)

def editsubmit(request, number):
    if request.method == 'POST':
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            print('you have error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/post/'+ number)
        else:   
            idnumber = number
            post = request.POST['post']
            postx = Post.objects.get(id=idnumber)
            postx.post = post
            postx.save()
            return redirect('/post')
    else:
        return redirect('/post/'+ number)