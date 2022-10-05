from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *

def index(request):
    
    context={
'all_books': Book.objects.all()
    }
    return render (request,"index.html",context)

def add (request):
    Book.objects.create(title=request.POST['title'], description=request.POST['desc'])
    return redirect ("/")

def viewbook(request,id):
    context={
        'onebook':Book.objects.get(id=id),
        'all_authors':Author.objects.all()
    }
    return render (request,"index2.html",context)

def authbook(request,id):
    mybook= Book.objects.get(id=id)
    myauthor=Author.objects.get(id=request.POST['authors'])
    mybook.authors.add(myauthor)

    return redirect ("/books/"+str(id))


def index3(request):
    
    context={
'all_authors': Author.objects.all()
    }
    return render (request,"index3.html",context)

def add2 (request):
    Author.objects.create(first_name=request.POST['first_name'],
    last_name=request.POST['last_name'],nots=request.POST['notes'])
    return redirect ("/author")

def viewauthor(request,id):
    all_books=Book.objects.all()
    oneauthor=Author.objects.get(id=id)
    context={
        'oneauthor':Author.objects.get(id=id),
        'all_books':Book.objects.all(),
        'all':oneauthor.books.all(all_books)
    }
    return render (request,"index4.html",context)

def authbook(request,id):
    myauthor= Book.objects.get(id=id)
    mybook=Author.objects.get(id=request.POST['books'])
    mybook.books.add(myauthor)
    return redirect ("/authors/"+str(id))





