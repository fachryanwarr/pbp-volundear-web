from django.http import HttpResponse
from django.shortcuts import render
from daftarrelawan.forms import DaftarRelawanForm
from daftarrelawan.models import DaftarRelawan
import datetime

from django.urls import reverse

# Create your views here.
def daftar_relawan(request):
    if request.method == "POST":
        form = DaftarRelawanForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse("OK")
            return response
    

    context = {}
    context['form'] = DaftarRelawanForm()
    return render(request, 'daftarrelawan.html', context)