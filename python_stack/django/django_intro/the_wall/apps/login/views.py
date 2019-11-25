from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'login/index.html')

def registration(request):
    if request.method == 'POST':
        errors = User.objects.regis_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['first'] = request.POST['first_name']
            last = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            hash_pass = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.session['first'], last_name=last, username=username, email=email, password=hash_pass.decode())
            userx = User.objects.get(email=email)
            request.session['idnumber'] = userx.id
            request.session['username'] = userx.username
            return redirect('/wall')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            usery = User.objects.get(email=request.POST['email_check'])
            request.session['first'] = usery.first_name
            request.session['idnumber'] = usery.id
            request.session['username'] = usery.username
            return redirect('/wall')
