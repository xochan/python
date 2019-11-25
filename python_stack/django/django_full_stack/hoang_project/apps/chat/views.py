from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    userx = User.objects.get(id=request.session['idnumber'])
    context = {
        'name': userx.first_name,
        'idnumber': userx.id,
        'all_friend': userx.friends.all(),
        'friend_count': len(userx.friends.all()),
        'chats': Chat.objects.filter(members=userx)
    }
    return render(request, 'chat/index.html', context)

def chat_create(request, real, idnumber):
    real_user = User.objects.get(id=real)
    userx = User.objects.get(id=idnumber)
    try:
        chat=Chat.objects.filter(members=userx).filter(members=real_user)[0]
        if chat:
            return redirect('/chat/message/'+str(chat.id))
    except:
        print('making new chat for ',real_user.first_name,'and',userx.first_name)   
    chatx = Chat.objects.create(name=userx.first_name)
    chatx.members.add(real_user)
    chatx.members.add(userx)
    return redirect('/chat/message/'+str(chatx.id))

def chat(request, id):
    chatx = Chat.objects.get(id=id)
    real_user = User.objects.get(id=request.session['idnumber'])
    context = {
        #'chat_name': chatx.name,
        #'real_name': real_user.first_name,
        #'x_name': userx.first_name,
        'real_user': real_user,
        'chat_id': chatx.id,
        'chat_messages': chatx.messages.all()
    }
    return render(request, 'chat/chat.html', context)

def message(request):
    real_user = User.objects.get(id=request.session['idnumber'])
    chat_id = request.POST['chat_id']
    #idnumber = request.POST['idnumber']
    chatx = Chat.objects.get(id=chat_id)


    Message.objects.create(message=request.POST['message'], user= real_user, chat= chatx)
    return redirect('/chat/message/'+str(chatx.id))
