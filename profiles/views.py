from django.shortcuts import render, redirect
from .models import DetailedUserData
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from profiles.models import DetailedUserData
from django.http import HttpResponse, JsonResponse
from django.core import serializers

@login_required(login_url='/auth/login/')
def show_profile(request):
    current_user = auth.get_user(request)

    account = DetailedUserData.objects.filter(user=request.user)
    if len(account) == 0:
        return redirect('profiles:show_edit')
    
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

@csrf_exempt
@login_required(login_url='/auth/login/')
def edit(request):
    if request.method == "POST":
        nama = request.POST.get('nama')
        tanggal_lahir = request.POST.get('tanggal_lahir')
        gender = request.POST.get('gender')
        telp = request.POST.get('telp')
        alamat = request.POST.get('alamat')
        pekerjaan = request.POST.get('pekerjaan')

        detailUser = DetailedUserData.objects.create(user=request.user, name=nama, gender=gender, phone_number=telp, pekerjaan=pekerjaan, alamat=alamat, tanggal_lahir=tanggal_lahir)
        detailUser.save()
        
        return redirect('profiles:show_profile')

@login_required(login_url='/auth/login/')
def show_edit(request):
    content = {}
    
    return render(request, "edit.html", content)

def get_detail(request):
    detail = DetailedUserData.objects.filter(user=request.user)

    hasil = {
            'fields':{
                'nama':detail[0].name,
                'gender':detail[0].gender,
                'phone_number':detail[0].phone_number,
                'pekerjaan':detail[0].pekerjaan,
                'alamat':detail[0].alamat,
                'tanggal_lahir':detail[0].tanggal_lahir,
            },
            'pk':detail[0].pk
        }

    return JsonResponse(hasil)

def get_profiles(request):
    profiles = DetailedUserData.objects.all()

    return HttpResponse(serializers.serialize("json", profiles), content_type="application/json")




