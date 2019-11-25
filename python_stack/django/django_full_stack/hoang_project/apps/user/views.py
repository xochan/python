from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from apps.login.models import User
from apps.post.models import Post

def user_infor(request,number):
    userx = User.objects.get(id=number)
    real_user = User.objects.get(id=request.session['idnumber'])
    context = {
        'name': userx.first_name,
        'real_name': real_user.first_name,
        'idnumber': userx.id,
        'posts': userx.posts.all().order_by('-created_at'),
        'all_user': User.objects.all(),
        'count': len(userx.friends.all()),
        'admin': real_user.admin,
        'friends': real_user.friends.filter(id=number)
    }
    return render(request, 'user/user_infor.html', context)

def friend(request, number):
    userx = User.objects.get(id=number)
    real_user = User.objects.get(id=request.session['idnumber'])
    context = {
        'name': userx.first_name,
        'real_name': real_user.first_name,
        'idnumber': userx.id,
        'posts': userx.posts.all(),
        'all_user': User.objects.all(),
        'all_friend': userx.friends.all(),
        'friend_count': len(userx.friends.all()),
        # 'all_follow': userx.follower.all(),
        # 'follow_count': len(userx.follower.all())
    }
    return render(request, 'user/friendlist.html', context)

def checkfriend(request):
    if request.method == 'POST':
        errors = User.objects.friend_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/' + request.POST['idnumber'])
        else:
            user_friend = User.objects.get(username=request.POST['username'])
            return redirect('/user/' + str(user_friend.id) )

def post_post(request):
    if request.method == 'POST':
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            iduser = request.POST['iduser']
            return redirect('/user/'+iduser)
        else:   
            post = request.POST['post']
            iduser = request.POST['iduser']
            userx = User.objects.get(id=iduser)
            Post.objects.create(user=userx, post=post)
            return redirect('/user/'+iduser)

def remove_post(request):
    idnumber = request.POST['idnumber']
    postx = Post.objects.get(id=idnumber)
    postx.delete()
    return redirect('/user/'+ str(postx.user.id))

def edit(request, number):
    postx = Post.objects.get(id=number)
    context = {
        'idnumber': number,
        'post' : postx.post,
        'time': postx.created_at
    }
    return render(request, 'user/edit.html', context)

def editsubmit(request):
    if request.method == 'POST':
        errors = Post.objects.post_validator(request.POST)
        if len(errors) > 0:
            print('you have error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/'+ request.POST['idnumber']+'/edit')
        else:   
            idnumber = request.POST['idnumber']
            post = request.POST['post']
            postx = Post.objects.get(id=idnumber)
            postx.post = post
            postx.save()
            return redirect('/user/'+ str(postx.user.id))

def add_friend(request):
    userx = User.objects.get(id=request.POST['idnumber'])
    real_user = User.objects.get(id=request.session['idnumber'])
    real_user.friends.add(userx)
    return redirect('/user/'+ str(userx.id))

def delete_friend(request):
    userx = User.objects.get(id=request.POST['idnumber'])
    real_user = User.objects.get(id=request.session['idnumber'])
    real_user.friends.remove(userx)
    return redirect('/user/'+ str(userx.id))

# def add_follow(request):
#     userx = User.objects.get(id=request.POST['idnumber'])
#     real_user = User.objects.get(id=request.session['idnumber'])
#     real_user.follower.add(userx)
#     return redirect('/user/'+ str(userx.id))

# def delete_follow(request):
#     userx = User.objects.get(id=request.POST['idnumber'])
#     real_user = User.objects.get(id=request.session['idnumber'])
#     real_user.follower.remove(userx)
#     return redirect('/user/'+ str(userx.id))