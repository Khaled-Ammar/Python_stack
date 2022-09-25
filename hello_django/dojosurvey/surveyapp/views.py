from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def form(request):
    return render(request, 'dojosurvey.html')
    
def dojo_form(request):
    if request.method == 'POST':
        context = {
        'uname': request.POST['Username'],
        'loc': request.POST['Location'],
        'favlang': request.POST['fav_lang'],
        'com': request.POST['Comment']
    }
        return render(request, 'index.html', context)
    else:
        return redirect('/')
