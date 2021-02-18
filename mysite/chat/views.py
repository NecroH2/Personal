from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
#from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CreateUserForm, CreateCuenta
from .models import CuentaU, Mensajes, Chats
from datetime import datetime, timedelta
from django.contrib.auth.models import Group
import random

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'chat/chats.html', {})
    else:
        return redirect('/login')


def registro(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Cuenta fue creada')
            return redirect('login')


    context = {'form':form}
    return render(request, 'registration/regisesion.html', context)


def confirmacion(request):
    return render(request, 'chat/confirmacion.html', {})


def nuevacuenta(request):

    data = {
        'form' : CreateCuenta()  
    }

    if request.method == 'POST':
        form = CreateCuenta(data=request.POST, files=request.FILES)
        if form.is_valid():
            tsk = form.save(commit=False)
            tsk.iduser = request.user
            form.save()
            return redirect(to='login')
        else:
            data["form"] = form

    return render(request, 'chat/creacion.html', data)


#def crearflujo(request):
#
#    data = {
#        'form' : CreateFlujo()  
#    }
#
#    if request.method == 'POST':
#        form = CreateFlujo(data=request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect(to='flujos')
#        else:
#            data["form"] = form
#
#    return render(request, 'blog/nuevoflujo.html', data)


# Create your views here.
