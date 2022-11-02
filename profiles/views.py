from django.shortcuts import render, redirect
from .models import DetailedUserData
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth


# Create your views here.
@login_required(login_url='/auth/login/')
def show_profile(request):
    current_user = auth.get_user(request)

    account = DetailedUserData.objects.filter(user=request.user)
    if len(account) == 0:
        return redirect('profiles:edit')
    
    if current_user.is_relawan:
        return redirect('profiles:profile_relawan')
    elif current_user.is_PJ:
        return redirect('profiles:profile_PJ')
    else:
        return redirect('landingpage:show_landingpage')

def profile_relawan(request):
    account = DetailedUserData.objects.filter(user=request.user)
    response = {'account':account}
    return render(request, 'profile_relawan.html', response)

def profile_PJ(request):
    account = DetailedUserData.objects.filter(user=request.user)
    response = {'account':account}
    return render(request, 'profile_PJ.html', response)

def profile_admin(request):
    account = DetailedUserData.objects.filter(user=request.user)
    response = {'account':account}
    return render(request, 'AdminProfile.html', response)

