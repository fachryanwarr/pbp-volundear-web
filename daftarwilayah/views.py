from urllib.request import Request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers
from django.contrib import auth
from daftarwilayah.models import Wilayah
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from authentication.decorators import relawan_required, PJ_required

def show_wilayah(request):
    content = {}
    
    return render(request, "daftarwilayah.html", content)

def get_wilayah(request):
    wilayah_items = Wilayah.objects.all()

    return HttpResponse(serializers.serialize("json", wilayah_items), content_type="application/json")

@login_required(login_url='/auth/login/')
@csrf_exempt
def add_wilayah(request):
    current_user = auth.get_user(request)

    if (not current_user.is_PJ):
        hasil = {
            'status':True
        }
        return JsonResponse(hasil)

    if request.method == "POST":
        name = request.POST.get('name')
        kota = request.POST.get('kota')
        address = request.POST.get('address')
        kuota_max = request.POST.get('kuota_max')
        description = request.POST.get('description')
        kebutuhan = request.POST.get('kebutuhan')
        awal_periode = request.POST.get('awal_periode')
        akhir_periode = request.POST.get('akhir_periode')


        wilayah = Wilayah.objects.create(pj=request.user, name=name, kota=kota, address=address,
            kuota_max=kuota_max, description=description, kebutuhan=kebutuhan, awalPeriode=awal_periode, akhirPeriode=akhir_periode)
        
        hasil = {
            'fields':{
                'name':wilayah.name,
                'kota':wilayah.kota,
                'address':wilayah.address,
                'kuota_max':wilayah.kuota_max,
                'description':wilayah.description,
                'kebutuhan':wilayah.kebutuhan,
                'jangka_waktu':wilayah.jangka_waktu
            },
            'pk':wilayah.pk,
            'status':False
        }

    return JsonResponse(hasil)

def get_wilayah_detail(request, id):
    wilayah = Wilayah.objects.get(pk = id)

    hasil = {
            'fields':{
                'name':wilayah.name,
                'kota':wilayah.kota,
                'kebutuhan':wilayah.kebutuhan,
                'address':wilayah.address,
                'kuota_max':wilayah.kuota_max,
                'kuota_terisi':wilayah.kuota_terisi,
                'description':wilayah.description,
                'jangka_waktu':wilayah.jangka_waktu,
            },
            'pk':wilayah.pk
        }
    return JsonResponse(hasil)

def get_daftar_kota(request):
    list_wilayah = Wilayah.objects.all()

    set_kota = []
    for wilayah in list_wilayah:
        set_kota.append(wilayah.kota)

    set_kota = set(set_kota)
    list_kota = list(set_kota)

    hasil = {
        'list_kota':list_kota,
    }

    return JsonResponse(hasil)

