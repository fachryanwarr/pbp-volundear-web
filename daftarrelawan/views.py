from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.urls import reverse
from daftarwilayah.models import Wilayah
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from daftarrelawan.models import Pendaftaran
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from django.urls import reverse

def daftar_relawan(request, id):
    if request.user.is_relawan:
        wilayah = Wilayah.objects.get(pk=id)

        nama_wilayah = wilayah.name
        kuota_terisi = wilayah.kuota_terisi
        kuota_max = wilayah.kuota_max
        wilayah_pk = wilayah.pk

        content = {
            "nama_wilayah" : nama_wilayah,
            "kuota_terisi" : kuota_terisi,
            "kuota_max" : kuota_max,
            "wilayah_pk" : wilayah_pk,
        }

        return render(request, "form_pendaftaran.html", content)
    else:
        context = {}
        return redirect('daftarwilayah:show_wilayah')
    
def get_pendaftaran(request):
    pendaftaran_items = Pendaftaran.objects.all()

    return HttpResponse(serializers.serialize("json", pendaftaran_items), content_type="application/json")

@csrf_exempt
def make_data(request):
    id = request.POST.get('pk')

    wilayah = Wilayah.objects.get(pk=id)
    current_user = auth.get_user(request)

    if request.method == "POST":
        keahlian = request.POST.get('keahlian')
        awal = request.POST.get('awal')
        akhir = request.POST.get('akhir')

        pendaftaran = Pendaftaran.objects.create(wilayah=wilayah, relawan=current_user, keahlian=keahlian, 
            mulai_periode=awal, akhir_periode=akhir)
        pendaftaran.save()
        
        wilayah.kuota_terisi += 1
        wilayah.save()

        return redirect('daftarwilayah:show_wilayah')
    else:
        return redirect('daftarwilayah:show_wilayah')


@csrf_exempt
def daftar_relawan_from_flutter(request, id):
    id = request.POST.get('pk')

    wilayah = Wilayah.objects.get(pk=id)
    current_user = auth.get_user(request)

    keahlian = request.POST.get('keahlian')
    awal = request.POST.get('awal')
    akhir = request.POST.get('akhir')

    pendaftaran = Pendaftaran.objects.create(wilayah=wilayah, relawan=current_user, keahlian=keahlian, 
        mulai_periode=awal, akhir_periode=akhir)
    pendaftaran.save()
    

    return JsonResponse()