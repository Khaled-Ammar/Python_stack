from multiprocessing import context
import bcrypt
from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
from time import gmtime, strftime


def index(request):
    return render (request , 'index.html')

# -----------------------renderhtmlpage-----------------------

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
        return render (request , 'all.html')
    else:
        return redirect('/')
# ------------------------------------success regist----------------------

def login(request):
    user = User.objects.filter(email=request.POST['log_email'])
    if user:
        logged_user = user[0]
        request.session['id'] = logged_user.id
        if bcrypt.checkpw(request.POST['log_pass'].encode(), logged_user.password.encode()):
            request.session['first_name'] = logged_user.first_name
            request.session['WhatWeDo']='Successfully Logged in'
            return redirect('/toall')
        else:
            messages.error(request , 'Email or Password is incorrect')
        return redirect('/')
    return redirect('/')

# -----------------------login_views-----------------

def logout(request):
    del request.session['first_name']
    return redirect('/')

def toindex1(request):
    return render (request , 'index1.html')

def toall(request):
    context ={
        'All' : Plan.objects.all(),
    }
    return render (request , 'all.html',context)


# -----------------------------------------------
def index1 (request):
    return render (request , 'index1.html')

def table(request):
    context ={
        'All' : Plan.objects.all(),
    }
    return render (request,'all.html',context)

def details(request):
    errors = Plan.objects.basic_validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, v in errors.items():
            messages.error(request, v)
        return redirect ('toindex1')
    else:
        user=User.objects.get(id= request.session['id'])
        Plan.objects.create(Species=request.POST['Species'],user=user,relaseDate=request.POST['date'],location=request.POST['location'])
        return redirect('/toall')

# -------------------------------------------------------------------

def show (request,id):
    context = {
        "time": strftime("%d %B, %Y ,%H:%M", gmtime()),
        'Plan' : Plan.objects.get(id = int(id)),
    }
    return render (request,'details.html',context )

# --------------------------------------------------------------------

def edit (request , id):
    context={
        'Plan' : Plan.objects.get(id=int(id))
    }
    return render ( request ,'editing.html' , context)

def update(request , id):
    errors = Plan.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, v in errors.items():
            messages.error(request, v)
        return redirect ('/plans/'+str(id)+'/edit')
    else:
        Nplan = Plan.objects.get(id = int(id))
        Nplan.Species=request.POST['Species']
        Nplan.Planted_By=request.POST['Planted_By']
        Nplan.relaseDate=request.POST['date']
        
        Nplan.save()
        return redirect ('/plans/' + str(id)+'/edit')

def destroy(request,id):
    show = Plan.objects.get(id=int(id))
    show.delete()
    return redirect ('/mytree')
def treeshow(request,id):
    context={
    'plan':Plan.objects.get(id=id)   }
    return render(request,'details.html',context)
def my(request):
    context={'user': User.objects.get(id=request.session['id'])}
    return render(request,'my.html',context)


    



