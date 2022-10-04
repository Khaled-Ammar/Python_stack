from django.shortcuts import render, HttpResponse, redirect
import random
from django.utils.timezone import datetime

def gold(request):
    if 'money' not in request.session or 'activities' not in request.session:
        request.session['money'] =0
        request.session['activities'] = []
    return render(request, 'index.html')

def processMoney(request):
    if request.POST['money']=='farm':
        randomNum = random.randint(10,20)
        request.session['money'] +=randomNum
        request.session['activities'].append('You entered a farm' +" "+ ' and earned ' +     str(randomNum)   +". "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')
        request.session['count']=randomNum
    elif request.POST['money']=='cave':
        randomNum = random.randint(10,20)
        request.session['money'] +=randomNum
        request.session['activities'].append('You entered a cave' +" "+ ' and earned ' +     str(randomNum)   +". "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')
    elif request.POST['money']=='house':
        randomNum = random.randint(10,20)
        request.session['money'] +=randomNum
        request.session['activities'].append('You entered a house' +" "+ ' and earned ' +str(randomNum)   +". "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')
    else:
        randomNum = random.randint(-50, 50)
        if randomNum > 0:
            request.session['activities'].append('You entered a quest' +" "+ ' and earned'+" " + str(randomNum)+". "+ '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')
        elif randomNum < 0:
            request.session['activities'].append('You failed a quest'+" "+ ' and lost' +" "+ str(randomNum)+ ".Ouch." '(' + str(datetime.now().strftime("%b-%d-%Y %H:%M-%p")) + ')')

        request.session['money'] +=randomNum
    return redirect('/')
    
def reset(request):
    request.session['money'] =0
    request.session['activities'] = []
    return redirect('/')