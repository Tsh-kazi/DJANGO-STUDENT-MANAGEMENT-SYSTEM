from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from .forms import UserRegisterForm



def index(request):
	return render(request, 'index.html')


def register(request):
	return render(request, 'register.html')


def login(request):
	pass

def panel(request):
	return render(request, 'panel.html')


def dashboard(request):
	return render(request, 'index.html')


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		form.save()
		messages.success(request, f'User Account Created successfully')
		return render(request, 'Registration/signup.html', {'form' : form})
	else:
		form = UserCreationForm()
	return render(request, 'Registration/signup.html', {'form' : form})

	