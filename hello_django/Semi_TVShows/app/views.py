from django.shortcuts import render,redirect
from .models import *

def root(request):
    return redirect('shows/news')

def indexAdd(request):
    return render(request,'add.html')

def add(request):
    Shows.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['date'],description=request.POST['desc'])
    return redirect('/shows/'+str(Shows1.objects.get(title=request.POST['title']).id))

def showDetail(request,id):
    context={'show':Shows.object.get(id=id)}
    return render(request,'showDetail.html',context)

