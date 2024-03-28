from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login,logout
from django.contrib import messages
from .models import *
from .forms import *
from django.conf import settings


# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2','')
        #print(username,email,password,password2) 
        if password != password2:
            return HttpResponse("your password is not same!")
        else:       
            data = User.objects.create_user(username,email,password)
            data.save()
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        #print(username,password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
          dj_login(request,user)
          return redirect('index')
        else:
            return HttpResponse("your username and password is incorrect")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('index')