from urllib.request import Request
from django import forms
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from django.core import serializers
from daftarwilayah.models import Wilayah

def show_wilayah(request):
    content = {}
    
    return render(request, "daftarwilayah.html", content)

def get_wilayah(request):
    wilayah_items = Wilayah.objects.all()

    return HttpResponse(serializers.serialize("json", wilayah_items), content_type="application/json")