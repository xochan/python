from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from apps.login.models import User

def wall(request):
    context = {
        'first' : request.session['first'],
        'idnumber' : request.session['idnumber'],
        'username': request.session['username'],
        'messages': Message.objects.all().order_by('-created_at'),
        'comments':  Comment.objects.all()
    }
    return render(request, 'first_wall/wall.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def post_message(request):
    if request.method == 'POST':
        request.session['idmessage'] = request.POST['idnumber']
        message = request.POST['message']
        userx = User.objects.get(id=request.session['idmessage'])
        Message.objects.create(message=message, user=userx)
        return redirect('/wall')

def post_comment(request):
    if request.method == 'POST':
        idmessage = request.POST['idmessage']
        print(idmessage)
        comment = request.POST['comment']
        messagex = Message.objects.get(id=idmessage)
        userx = User.objects.get(id=request.session['idnumber'])
        Comment.objects.create(comment=comment, user=userx,  message=messagex)
        return redirect('/wall')

def delete_message(request, number):
    if request.method == 'POST':
        messagex = Message.objects.get(id=number)
        messagex.comments.all().delete()
        messagex.delete()
        return redirect('/wall')

def delete_comment(request, number):
    if request.method == 'POST':
        commentx = Comment.objects.get(id=number)
        commentx.delete()
        return redirect('/wall')