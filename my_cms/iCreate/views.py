from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'iCreate/index.html')


def login(request):
    return render(request, 'iCreate/login.html')


def register(request):
    return render(request, 'iCreate/register.html')

def recover_pw(request):
    return render(request, 'iCreate/pw-recovery.html')