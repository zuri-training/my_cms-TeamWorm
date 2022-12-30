from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from account.forms import RegistrationForm

# Create your views here.
def home_screen_view(request):
	context = {}
	return render(request, "index.html", context)


def login(request):
    return render(request, 'account/login.html')

# def register(request):
#     return render(request, 'account/register.html')

def recover_pw(request):
    return render(request, 'account/pw-recovery.html')


def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated:
		return redirect('home')

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('home')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

