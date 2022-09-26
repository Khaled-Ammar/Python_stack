from multiprocessing import context
from django.shortcuts import render,HttpResponse
from .models import User

def root(request):
    
    context={
            'all_user':User.objects.all()}
    return render(request,'index.html',context)
    
def handle(request):
    User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email_address=request.POST['email'], age = request.POST['age'])
    return redirect('/')
