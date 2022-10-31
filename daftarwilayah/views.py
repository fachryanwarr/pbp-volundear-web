from urllib.request import Request
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from daftarwilayah.models import Wilayah
from django.views.decorators.csrf import csrf_exempt

def show_wilayah(request):
    content = {}
    
    return render(request, "daftarwilayah.html", content)

def get_wilayah(request):
    wilayah_items = Wilayah.objects.all()

    return HttpResponse(serializers.serialize("json", wilayah_items), content_type="application/json")

@csrf_exempt
def add_wilayah(request):
    if request.method == "POST":
        name = request.POST.get('name')
        kota = request.POST.get('kota')
        address = request.POST.get('address')
        kuota_max = request.POST.get('kuota_max')
        description = request.POST.get('description')
        kebutuhan = request.POST.get('kebutuhan')
        jangka_waktu = request.POST.get('jangka_waktu')

        wilayah = Wilayah.objects.create(user=request.user, name=name, kota=kota, address=address,
            kuota_max=kuota_max, description=description, kebutuhan=kebutuhan, jangka_waktu=jangka_waktu)
        
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
            'pk':wilayah.pk
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

