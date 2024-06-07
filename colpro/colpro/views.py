from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. this is the Home page")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("Hello, world. this is the about page")

def contact(request):
    return HttpResponse("Hello, world. this is the contact page")