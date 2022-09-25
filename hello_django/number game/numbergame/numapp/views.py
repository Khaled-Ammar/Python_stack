from django.shortcuts import render , redirect
import random

def Number(request):
    request.session['random'] = random.randint(1, 100)
    request.session['result']=''
    return render (request , 'index.html')

def result(request):
    RandomNumber = request.session['random']
    request.session['num'] = RandomNumber
    YourNumber = int(request.POST['number'])
    if YourNumber == RandomNumber:
        request.session['result'] = "Great Guess"
    elif YourNumber > RandomNumber:
        request.session['result'] = "High"
    elif YourNumber < RandomNumber:
        request.session['result'] = "Looooow"
    return redirect ('/show')

def res(request):
    return render (request , 'index.html')

def PlayAgian(request):
    return redirect ('/')