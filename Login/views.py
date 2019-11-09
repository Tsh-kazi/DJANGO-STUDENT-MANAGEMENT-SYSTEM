from django.http import HttpResponse
from django.shortcuts import render
import datetime
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'Template/index.html')

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


def login(request):
    return render(request, '_login.html')


def panel(request):
    return render(request, 'panel.html')


def registration(request):
    return render(request, 'registration.html')

def recover(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'recover.html')