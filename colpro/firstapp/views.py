from django.shortcuts import render

# Create your views here.
def all_first(request):
    return render(request, 'firstapp/all_first.html')
