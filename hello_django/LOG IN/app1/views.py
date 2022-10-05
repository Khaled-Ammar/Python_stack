import bcrypt
from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render (request , 'index.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash=bcrypt.hashpw(password.encode() , bcrypt.gensalt()).decode()
        User.objects.create(first_name = request.POST['first_name'] , last_name=request.POST['last_name'], 
            email=request.POST['email'] , password = pw_hash )
        request.session['first_name']=User.objects.last().first_name
        request.session['WhatWeDo']='Successfully Registered'
        return redirect('/success')

def success(request):
    if 'first_name' in request.session:
        return render (request , 'success.html')
    else:
        return redirect('/')

def login(request):
    user = User.objects.filter(email=request.POST['log_email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['log_pass'].encode(), logged_user.password.encode()):
            request.session['first_name'] = logged_user.first_name
            request.session['WhatWeDo']='Successfully Logged in'
            return redirect('/success')
        else:
            messages.error(request , 'Email or Password is incorect')
        return redirect('/')
    return redirect('/')

def logout(request):
    del request.session['first_name']
    return redirect('/')