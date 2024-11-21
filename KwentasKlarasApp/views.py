from django.shortcuts import render
from django.conf.urls import handler404

def login(request):
    return render(request, 'login.html')

def index(request):
    context = {}
    return render(request, 'index.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = 'KwentasKlarasApp.views.custom_404'  # Replace 'myapp' with your app's name

