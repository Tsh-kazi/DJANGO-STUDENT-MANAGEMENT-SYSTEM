from django.urls import path, include
from . import views



urlpatterns = [
	path('', views.index),
	#path('login', views.login),
	path('register', views.register),
	path('panel', views.panel),
	path('dashboard', views.dashboard),
	path('signup', views.signup),

]
