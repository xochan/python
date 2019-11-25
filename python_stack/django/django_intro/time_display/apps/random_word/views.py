from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
from time import gmtime,strftime

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter']= 0
    if 'word' not in request.session:
        request.session['word'] =[]

    context ={
        'counter': request.session['counter'],
        'word': request.session['word']
    }
    # return render(request,'random_word/index.html',word = request.session['word'],counter=request.session['counter'])
    return render(request,'random_word/index.html',context)
def random(request):
    # if request.method == "GET":
    # 	print(request.GET)
    if request.method == "POST":
        print(request.POST)
        # request.session['word']=request.POST['generate']
        request.session['word']=get_random_string(length=10)
        request.session['counter'] += 1
    return redirect('/random_word')

def reset(request):
    if request.method == "POST":
        request.session.pop('counter')
        # request.session['counter'] -= 1
    return redirect('/random_word')