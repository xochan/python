from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'game/index.html')

def pacman(request):
    return render(request, 'game/pacman.html')