from multiprocessing import context
import bcrypt
from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
import bcrypt
from time import gmtime, strftime

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
        request.session['id'] = logged_user.id
        if bcrypt.checkpw(request.POST['log_pass'].encode(), logged_user.password.encode()):
            request.session['first_name'] = logged_user.first_name
            request.session['WhatWeDo']='Successfully Logged in'
            return redirect('/MainPage')
        else:
            messages.error(request , 'Email or Password is incorect')
        return redirect('/')
    return redirect('/')

def logout(request):
    del request.session['first_name']
    return redirect('/')


def mainpage(request):
    user1 = User.objects.get(id=request.session['id'])
    context={
        'u': User.objects.get(id=request.session['id']),
        'user' : User.objects.get(id=request.session['id']).first_name,
        'books' : User.objects.get(id=request.session['id']).books_uploded.all(),
        'booksall': Book.objects.all(),
        'favBooks' : User.objects.get(id=request.session['id']).liked_books.all(),
        'userFav' : user1.liked_books.all(),
    }
    return render (request , 'main.html' , context)

def fav(request):
        user1 = User.objects.get(id=request.session['id'])
        Book.objects.create(title=request.POST['title'],desc=request.POST['Descreption'],uploaded_by=user1)
        Book.objects.get(title =request.POST['title']).users_who_like.add(user1)
        return redirect ('/MainPage')

def BookDetails(request , id):
    
    context={
        'u': User.objects.get(id=request.session['id']),
        'user' : User.objects.get(id=request.session['id']).first_name,
        'books' : User.objects.get(id=request.session['id']).books_uploded.all(),
        'booksall': Book.objects.all(),
        'favBooks' : User.objects.get(id=request.session['id']).liked_books.all(),
        'ourbook' : Book.objects.get(id=id),
        'thisbook' : Book.objects.get(id=id).users_who_like.all(),
        'time' : strftime("%d %B, %Y ,%H:%M", gmtime()),
        }
    return render (request ,'fav.html' , context )


def addToFav(request ,id):
    user1 = User.objects.get(id=request.session['id'])
    NewFav=Book.objects.get(id=id)
    NewFav.users_who_like.add(user1)
    return redirect ('/books/' +str(id))


def remove(request ,id ):
    user1 = User.objects.get(id=request.session['id'])
    RemoveFav=Book.objects.get(id=id)
    RemoveFav.users_who_like.remove(user1)
    return redirect ('/books/' +str(id))

def DeleteUpdate(request ,id):
    if request.POST['which'] == 'Delete' :
        Book.objects.get(id=id).delete()
        return redirect ('/MainPage')
    else :
        UpdBook=Book.objects.get(id=id)
        UpdBook.title=request.POST['newtitle']
        UpdBook.desc=request.POST['newdesc']
        UpdBook.save()
        return redirect ('/books/' + str(id))


def back(request):
    return redirect('/MainPage')
