from contextlib import redirect_stdout
from django.shortcuts import render,redirect
def index(request):
    if 'num' in request.session:
        request.session['num']+=1
    else:
        request.session['num']=1
    return render(request,'index.html')
def destroy(request):
    del request.session['num']
    return redirect('/')
def increment(request):
    request.session['num']+=1
    return redirect('/')






# Create your views here.
