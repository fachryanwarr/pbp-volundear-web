from multiprocessing import context
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib import auth
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import get_user
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from authentication.models import User


from django.contrib.auth import logout

import datetime

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse

from django.core import serializers

from django.contrib.auth.decorators import user_passes_test

from authentication.forms import RelawanSignUpForm, PJSignUpForm

def register(request):
    form = UserCreationForm()

    context = {'form':form}
    
    return render(request, 'register.html', context)

def register_relawan(request):
    form = RelawanSignUpForm()

    if request.method == "POST":
        form = RelawanSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('authentication:login')
    
    context = {'form':form}
    return render(request, 'register_relawan.html', context)

def register_PJ(request):
    form = PJSignUpForm()

    if request.method == "POST":
        form = PJSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('authentication:login')
    
    context = {'form':form}
    return render(request, 'register_PJ.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            response = HttpResponseRedirect(reverse("landingpage:show_landingpage"))

            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('landingpage:show_landingpage'))
    return response


@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)