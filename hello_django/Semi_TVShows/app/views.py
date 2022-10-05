from urllib import request
from django.shortcuts import render , redirect
from .models import *
from time import gmtime, strftime
from django.contrib import messages

def index (request):
    return render (request , 'index.html')

def table(request):
    context ={
        'All' : Show.objects.all()
    }
    return render (request,'all.html',context)

def details (request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, v in errors.items():
            messages.error(request, v)
        return redirect ('/')
    else:
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],relaseDate=request.POST['date'],description=request.POST['desc'])
        return redirect('/shows/'+str(Show.objects.get(title=request.POST['title']).id))

def show (request,id):
    context = {
        "time": strftime("%d %B, %Y ,%H:%M", gmtime()),
        'show' : Show.objects.get(id = int(id)),
    }
    return render (request,'details.html',context )

def edit (request , id):
    context={
        'show' : Show.objects.get(id=int(id))
    }
    return render ( request ,'editing.html' , context)

def update(request , id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, v in errors.items():
            messages.error(request, v)
        return redirect ('/shows/'+str(id)+'/edit')
    else:
        Nshow = Show.objects.get(id = int(id))
        Nshow.title=request.POST['title']
        Nshow.network=request.POST['network']
        Nshow.relaseDate=request.POST['date']
        Nshow.description=request.POST['desc']
        Nshow.save()
        return redirect ('/shows/' + str(id))

def destroy(request , id):
    show = Show.objects.get(id=int(id))
    show.delete()
    return redirect ('/shows')