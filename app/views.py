from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def appinfo(request):
    return render(request, 'infoapp.html')