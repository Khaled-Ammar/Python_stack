from contextlib import redirect_stderr 
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *

def index(request):
    context={
        'books':Book.objects.all()
    }
    return render(request,'index.html',context) 

def addbook(request):
    Book.objects.create(title=request.POST['title'])
    return redirect('/')

def viewbook(request,id):
    context={
    'book':Book.objects.get(id=int(id)),
    'allpublishers': Publisher.objects.all()
    }
    return render(request,'view.html',context)

def pubtobook(request,id):
    book1=Book.objects.get(id=int(id))
    pub1=Publisher.objects.get(id=request.POST['pubtobook'])
    book1.publishers.add(pub1)
    return redirect ('/books'+str(id))



# Create your views here.
