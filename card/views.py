from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Details
from bitcoin import *
import bs4
import requests

# from django.shortcuts import render, redirect
# from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
# from django.contrib.auth import logout
# from django.http import HttpResponse
# from django.contrib.auth.models import User, auth
# from django.contrib import messages
# from .models import CustomUser

def home(request):
    return render(request, 'home/home.html')

def receive(request):
    return render(request, 'receive/receive.html')

def send(request):
    return render(request, 'send/send.html')

def setting(request):
    return render(request, 'setting/setting.html')

def swap(request):
    return render(request, 'swap/swap.html')

def history(request):
    return render(request, 'history/history.html')

def index(request):
    return render(request, 'index/history.html')


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'auth/login.html')


def register(request):
    detail = Details()
    private_key = random_key()
    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    detail.private_key = private_key
    detail.public_key = public_key
    detail.address = address

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        private_key = request.POST['private_key']
        public_key = request.POST['public_key']
        address = request.POST['address']
        if password==password2:       
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, last_name=private_key, first_name=address)
                user.save();
                print('User Created')
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'auth/register.html', {'detail': detail})

def logout(request):
    auth.logout(request)
    return redirect('/')