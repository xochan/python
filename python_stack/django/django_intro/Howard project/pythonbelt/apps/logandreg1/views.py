from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'logandreg1/index.html')

def registration(request):
    if request.method == 'POST':
        errors = Registration.objects.regis_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['name'] = request.POST['name']
            email = request.POST['email']
            hash_pass = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt())
            Registration.objects.create(name=request.session['name'], email=email, password=hash_pass.decode())
            userx = Registration.objects.get(email=email)
            request.session['idnumber'] = userx.id
            return redirect('/groups')

def login(request):
    if request.method == 'POST':
        errors = Registration.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            usery = Registration.objects.get(email=request.POST['email_check'])
            request.session['name'] = usery.name
            request.session['email'] = usery.email
            request.session['idnumber'] = usery.id
            return redirect('/groups')