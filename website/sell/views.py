from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *



# Create your views here.



def Index(request):
    return render(request,'index.html')


