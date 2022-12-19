from django.shortcuts import render
from django.http import HttpResponse
from django.conf  import settings

# Create your views here.
user = settings.AUTH_USER_MODEL
def index(request):
    return render(request, 'index.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
