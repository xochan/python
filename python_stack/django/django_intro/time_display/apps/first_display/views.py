from django.shortcuts import render
from time import gmtime,strftime

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'first_display/index.html',context)
# def new(request):
#     return HttpResponse('placeholder to display a new form to creata a new blog')

# def create(request):
#     return redirect('/')

# def show(request,number):
#     return HttpResponse(f'placeholder to display blog number:{number}')

# def edit(request,number):
#     return HttpResponse(f'placeholder to edit blog {number}')

# def destroy(request,number):
#     return redirect('/')