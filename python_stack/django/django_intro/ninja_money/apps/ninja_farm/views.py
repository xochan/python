from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
    if 'message' not in request.session:
        request.session['message'] =[]
    context ={
        'gold': request.session['gold'],
        'message': request.session['message'],
    }
    # return render(request,'random_word/index.html',word = request.session['word'],counter=request.session['counter'])
    return render(request,'ninja_farm/index.html',context)

def farming(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
    if 'message' not in request.session:
        request.session['message'] =[]

    if request.method == 'POST':
        value = request.POST['pro']
        if value  == 'farm':
            num = random.randint(10,20)
            print(datetime.now())
            print(request.session['gold'])
            request.session['gold'] += num
            request.session['message'].insert(0,['earn ' + str(num)+ ' in farm at '+ str(datetime.now()),'blue'])
            # insert(0, [color, f"{building} earned you {gains} gold at {datetime.now()}"])
            print('+',num,'= ',request.session['gold'], '\n',"*"*40)
        if value  == 'cave':
            num = random.randint(5,10)
            print(request.session['gold'])
            request.session['gold'] += num
            request.session['message'].insert(0,['earn ' + str(num)+ ' in cave at '+ str(datetime.now()),'blue'])
            print('+',num,'= ',request.session['gold'], '\n',"*"*40)
        if value  == 'house':
            num = random.randint(2,5)
            print(request.session['gold'])
            request.session['gold'] += num
            request.session['message'].insert(0,['earn ' + str(num)+ ' in house at '+ str(datetime.now()),'blue'])
            print('+',num,'= ',request.session['gold'], '\n',"*"*40)
        if value  == 'casino':
            x = random.randint(1,2)
            if x == 1:
                num = random.randint(0,50)
                print(request.session['gold'])
                request.session['gold'] += num
                request.session['message'].insert(0,['earn ' + str(num)+ ' in casino at '+ str(datetime.now()),'blue'])
                print('+',num,'= ',request.session['gold'], '\n',"*"*40)
            if x == 2:
                num = random.randint(0,50)
                print(request.session['gold'])
                request.session['gold'] -= num
                request.session['message'].insert(0,['take ' + str(num)+ ' in casino at '+ str(datetime.now()),'red'])
                print('+',num,'= ',request.session['gold'], '\n',"*"*40)
    return redirect('/')

def reset(request):
    request.session.pop('gold')
    request.session.pop('message')
    return redirect('/')