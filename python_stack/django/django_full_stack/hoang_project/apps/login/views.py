from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'login/index.html')

def registration(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            username = request.POST['username']
            birthday = request.POST['birthday']
            hash_pass = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username, birthday= birthday, password=hash_pass.decode())
            userx = User.objects.get(email=email)
            request.session['idnumber'] = userx.id
            return redirect('/post')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            usery = User.objects.get(email=request.POST['email_check'])
            request.session['idnumber'] = usery.id
            return redirect('/post')
