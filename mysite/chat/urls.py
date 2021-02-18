from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls import * 
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
#from blog.views import SignInView

urlpatterns = [
    path('', views.home_view, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('creacion/', views.nuevacuenta, name='nuevacuenta'),

]  