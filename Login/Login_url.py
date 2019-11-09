from . import views
from django.urls import path


urlpatterns = [
    path('', views.login),
    path('_login', views.login),
    path('panel.html', views.panel),
    path('registration.html', views.registration)
]




