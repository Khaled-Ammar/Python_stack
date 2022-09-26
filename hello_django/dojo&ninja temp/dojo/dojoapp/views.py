from os import stat
from django.shortcuts import render,HttpResponse,redirect
from .models import *


def root(request):
    context={
            'dojo':Dojo.objects.all()
            }
    return render(request,'index.html',context)
    
def handle(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')

def handle2(request):
    dojo1=Dojo.objects.get(id=request.POST['Dojo'])
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=dojo1)
    return redirect('/')




# Create your views here.
