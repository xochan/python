from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from apps.login.models import User
from django.db.models import Count

def group(request):
    userx = User.objects.get(id=request.session['id'])
    # orga_all = Organization.objects.all()
    # for orga in orga_all:
    #     member = orga.members
    #     count = count(member)
    #     list_orga = orga_all.order_by('count')
    # groupx = Group.objects.exclude(members = userx)
    context = {
        'user' : userx.first_name+' '+userx.last_name,
        'id' : request.session['id'],
        # 'list_orga' : orga_all.order_by(count)
        # 'organizations': Organization.objects.all().order_by('members')
        # 'organizations': Organization.objects.all().order_by('members__user')
        'organizations': Organization.objects.annotate(count=Count('members')).order_by('-count')
        # 'members': groupx
    }
    return render(request, 'group/group.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def create(request):
    if request.method == 'POST':
        errors = Organization.objects.organization_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.warning(request, value)
            return redirect('/group')
        else:   
            name = request.POST['name']
            description = request.POST['description']
            iduser = request.POST['iduser']
            userx = User.objects.get(id=iduser)
            organization = Organization.objects.create(user=userx, name=name, description=description)
            organization.members.add(userx)
            return redirect('/group')

def delete(request):
    idnumber = request.POST['idnumber']
    postx = Organization.objects.get(id=idnumber)
    if postx.user.id == request.session['id']:
        postx.delete()
        return redirect('/group')
    else:
        return redirect('/group')

def infor(request, idnumber):
    userx = User.objects.get(id=request.session['id'])
    organization = Organization.objects.get(id=idnumber)
    exclude = Organization.objects.exclude(members = userx)
    include = Organization.objects.filter(members = userx)
    context = {
        'id' : request.session['id'],
        'organizations': Organization.objects.all().order_by('-created_at'),
        'organization': organization,
        'members': organization.members.all(),
        'exclude': exclude,
        'include': include,
        'userx': userx
    }
    return render(request, 'group/infor.html', context)

# def join(request, idnumber):
#     userx = User.objects.get(id=request.session['id'])
#     organization = Organization.objects.get(id=idnumber)
#     members = organization.members.all()
#     if userx not in members:
#         organization.members.add(userx)
#         return redirect('/group/'+ idnumber)
#     else:
#         return redirect('/group/'+ idnumber)

# def leave(request, idnumber):
#     userx = User.objects.get(id=request.session['id'])
#     organization = Organization.objects.get(id=idnumber)
#     members = organization.members.all()
#     if userx in members:
#         organization.members.remove(userx)
#         return redirect('/group/'+ idnumber)
#     else:   
#         return redirect('/group/'+ idnumber)

def join_leave(request, idnumber):
    userx = User.objects.get(id=request.session['id'])
    organization = Organization.objects.get(id=idnumber)
    members = organization.members.all()
    if userx in members:
        organization.members.remove(userx)
        return redirect('/group/'+ idnumber)
    elif userx not in members:
        organization.members.add(userx)
        return redirect('/group/'+ idnumber)
    else:   
        return redirect('/group/'+ idnumber)