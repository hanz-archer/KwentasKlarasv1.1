from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def index(request):
    context = {}
    return render(request, 'index.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')


