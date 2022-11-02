from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from donasi.models import Donasi
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

# Create your views here.
# TODO:views menampilkan donasi 
def show_donasi(request):
    data_donasi = Donasi.objects.all()
    context = {
    'username' : request.user.username,
    'data' : data_donasi,
    }
    return render(request, "donasi.html", context)

# views untuk membuat donasi baru
@login_required(login_url="/auth/login/")
@csrf_exempt 
def create_donasi_ajax(request):
    if request.method == "POST":
        nama = request.POST.get('nama')
        jumlah = request.POST.get('jumlah')
        pesan = request.POST.get('pesan')
        # donasi = Donasi.objects.create(nama=nama, jumlah=jumlah, pesan=pesan, user=request.user)
        donasi = Donasi.objects.create(request.user, nama=nama, jumlah=jumlah, pesan=pesan)
        hasil = {'pk':donasi.pk,
                'fields':{
                'nama':donasi.nama,
                'jumlah':donasi.jumlah,
                'pesan':donasi.pesan,
        }}
    return JsonResponse(hasil)


# views untuk menampilkan donasi yang telah dibuat (tp bingung kalau semua user gmn tar cek lg)
# @login_required(login_url='/login/')
def show_json(request):
    donasi = Donasi.objects.all()
    return HttpResponse(serializers.serialize('json', donasi), content_type='application/json')


