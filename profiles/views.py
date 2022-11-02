from django.shortcuts import render, redirect
from .models import DetailedUserData
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from authentication.models import User
from profiles.forms import UpdateProfil
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
    return render(request, 'RelawanProfile.html', response)

def profile_PJ(request):
    account = DetailedUserData.objects.filter(user=request.user)
    response = {'account':account}
    return render(request, 'PJProfile.html', response)

def profile_admin(request):
    account = DetailedUserData.objects.filter(user=request.user)
    response = {'account':account}
    return render(request, 'AdminProfile.html', response)

@login_required(login_url='/auth/login/')
def edit(request, *args, **kwargs):
    context = {}
    if request.POST:
        form = UpdateProfil(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('profiles:show_profile')
        else :
            form = UpdateProfil(request.POST, instance= request.user,       
                    initial = {
                        "nama" : account.nama,
                        "jenis_kelamin" : account.jenis_kelamin,
                        "institusi" : account.institusi,
                        "email" : account.email,
                        "kontak" : account.kontak
                    }   
                ) 
            context['form'] = form
            return render(request, 'FormProfil.html', context)