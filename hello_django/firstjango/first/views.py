from django.shortcuts import render,HttpResponse,redirect

def hi(request):
    return HttpResponse("hello world")

def index(request):
    return HttpResponse("placeholder")

def new(request):
    return HttpResponse("placeholder2")

def redir(request):
    return redirect ("/")

def number (request,num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit (request,num):
    return HttpResponse(f"placeholder to edit blog: {num}")

def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})




