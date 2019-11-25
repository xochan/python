from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return HttpResponse('please go to /http://localhost:8000/shows')

def shows(request):
    context = {
        'all_show' : Show.objects.all()
    }
    return render(request, 'first_tvshow/shows.html', context)

def showinfor(request, num):
    showx = Show.objects.get(id = num)
    context = {
        'id' : showx.id,
        'title': showx.title,
        'network' : showx.network,
        'release_date' : showx.release_date,
        'desc' : showx.desc,
        'last_update': showx.updated_at,
        'all_show' : Show.objects.all()
    }
    return render(request, 'first_tvshow/showinfor.html', context)

def createshow(request):
    return render(request, 'first_tvshow/addnew.html')

def create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        release = request.POST['release']
        desc = request.POST['desc']
        new = Show.objects.create(title=title, network = network, release_date = release, desc=desc)
    return redirect('/shows/'+str(new.id))

def edit(request, num):
    showx = Show.objects.get(id = num)
    context = {
        'id' : showx.id,
        'title': showx.title,
        'network' : showx.network,
        'release_date' : showx.release_date,
        'desc' : showx.desc,
        'last_update': showx.updated_at,
        'all_show' : Show.objects.all()
    }
    return render(request, 'first_tvshow/update.html', context)

def update(request):
    errors = Show.objects.basic_validator(request.POST)
    idnumber = request.POST['id']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/'+str(idnumber)+'/edit')
    else:
        title = request.POST['title']
        network = request.POST['network']
        release = request.POST['release']
        desc = request.POST['desc']
        showedit = Show.objects.get(id=idnumber)
        showedit.title = title
        showedit.network = network
        showedit.release_date = release
        showedit.desc = desc
        showedit.save()
    return redirect('/shows/'+str(idnumber))

def delete(request, num):
    showdelete = Show.objects.get(id=num)
    showdelete.delete()
    return redirect('/shows')