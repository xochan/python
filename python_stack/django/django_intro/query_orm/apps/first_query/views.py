from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime
# Create your views here.
def index(request):

    return render(request,'first_query/index.html')