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



# Create your views here.
