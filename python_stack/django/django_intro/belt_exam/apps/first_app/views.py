from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from apps.login.models import User

def quote(request):
    userx = User.objects.get(id=request.session['idnumber'])
    quotex = Quote.objects.exclude(user_favorite = userx)
    context = {
        'name' : request.session['name'],
        'idnumber' : request.session['idnumber'],
        'quotes': Quote.objects.all().order_by('-created_at'),
        'user_favorite': userx.favorite_quote.all(),
        'quote_not_favorite': quotex
    }
    return render(request, 'first_app/quote.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def post_quote(request):
    if request.method == 'POST':
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/quote')
        else:   
            author = request.POST['author']
            quote = request.POST['quote']
            iduser = request.POST['iduser']
            userx = User.objects.get(id=iduser)
            Quote.objects.create(user=userx, author=author, quote=quote)
            return redirect('/quote')

def user_infor(request, number):
    userx = User.objects.get(id=number)
    request.session['count'] = 0
    quotes = userx.quotes.all()
    for quote in quotes:
        request.session['count'] += 1
    context = {
        'name': userx.name,
        'quotes': userx.quotes.all()
    }
    return render(request, 'first_app/user_infor.html', context)

def add_favorite(request):
    idnumber = request.POST['idnumber']
    quotex = Quote.objects.get(id=idnumber)
    userx = User.objects.get(id=request.session['idnumber'])
    userx.favorite_quote.add(quotex)
    return redirect('/quote')

def remove_favorite(request):
    idnumber = request.POST['idnumber']
    quotex = Quote.objects.get(id=idnumber)
    userx = User.objects.get(id=request.session['idnumber'])
    userx.favorite_quote.remove(quotex)
    return redirect('/quote')

def remove_quote(request):
    idnumber = request.POST['idnumber']
    quotex = Quote.objects.get(id=idnumber)
    quotex.delete()
    return redirect('/quote')

def edit(request, number):
    context = {
        'idnumber': number
    }
    print(number)
    return render(request, 'first_app/edit.html', context)

def editsubmit(request, number):
    if request.method == 'POST':
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors) > 0:
            print('you have error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/quote/'+ number)
        else:   
            idnumber = number
            author = request.POST['author']
            quote = request.POST['quote']
            quotex = Quote.objects.get(id=idnumber)
            quotex.author = author
            quotex.quote = quote
            quotex.save()
            return redirect('/quote')
    else:
        return redirect('/quote/'+ number)