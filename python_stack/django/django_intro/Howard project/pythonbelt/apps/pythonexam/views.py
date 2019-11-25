from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from apps.logandreg1.models import Registration


def groups(request):
    user = Registration.objects.get(id=request.session['idnumber'])
    groupy = Group.objects.exclude(user = user)
    context = {
        'all_groups': Group.objects.all(),
        'name' : request.session['name'],
        'idnumber' : request.session['idnumber'],
        'group': Group.objects.all().order_by('-created_at'),
        'user_groups': user.joined_groups.all(),
        'unjoined_groups': groupy
    }
    return render(request, 'pythonexam/groups.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def user_info(request, num):
    userx = Registration.objects.get(id=num)
    request.session['count'] = 0
    groups = userx.group.all()
    for groups in groups:
        request.session['count'] += 1
    context = {
        'name': userx.firstname,
        'groups': userx.groups.all()
    }
    return render(request, 'pythonexam/groups.html', context)


def add(request):
    if request.method == 'POST':
        errors = Group.objects.group_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/groups')
        else:
            name = request.POST['name']
            desc = request.POST['description']
            userx = Registration.objects.get(email=request.session['email'])
            this_org = Group.objects.create(name=name, desc=desc, user = userx)
            this_org.joined_users.add(userx)
            userx.joined_groups.add(this_org)
            this_org.save()
            return redirect('/groups')

def join_group(request):
    idnumber = request.POST['idnumber']
    groupx = Group.objects.get(id=idnumber)
    userx = Registration.objects.get(id=request.session['idnumber'])
    userx.related_group.remove(groupx)
    return redirect('/groups')

def leave_group(request):
    idnumber = request.POST['idnumber']
    groupx = Group.objects.get(id=idnumber)
    groupx.delete()
    return redirect('/groups')

def small_group(request, num):
    groupz = Group.objects.get(id=num)
    context={
        'all_members': groupz.joined_users.all(),
        'name': groupz.name,
        'desc': groupz.desc,
        'maker': groupz.user.name,
    }
    return render(request, 'pythonexam/smallgroup.html', context)
    