from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'login/index.html')

def registration(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            request.session['first'] = request.POST['first_name']
            last = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['pass']
            User.objects.create(first_name=request.session['first'], last_name=last, email=email, password=password)
            return redirect('/addsuccess')
def addsuccess(request):
    context = {
        'first' : request.session['first']
    }
    return render(request, 'login/success.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if User.objects.filter(email=request.POST['email_check'], password=request.POST['pass_check']):
        userx = User.objects.get(email=request.POST['email_check'])
        request.session['first'] = userx.first_name
        return redirect('/addsuccess')
    else:
        messages.info(request, "Login Unsuccessful")
        return redirect('/')