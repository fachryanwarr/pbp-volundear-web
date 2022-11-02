from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from daftarrelawan.forms import DaftarRelawanForm
from daftarrelawan.models import DaftarRelawan
from daftarwilayah.views import show_wilayah
import datetime

from django.urls import reverse

# Create your views here.
def daftar_relawan(request):
    if not DaftarRelawan.isRelawan:
        if request.method == "POST":
            form = DaftarRelawanForm(request.POST)
            if form.is_valid():
                form.save()
                response = HttpResponseRedirect(reverse("daftarwilayah:show_wilayah"))
                return response
        else:
            form = DaftarRelawanForm()
        context = {'form':form}
        return render(request, 'daftarrelawan.html', context)
        

    # context = {}
    # context['form'] = DaftarRelawanForm()
    # return render(request, 'daftarrelawan.html', context)