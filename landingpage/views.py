from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from landingpage.models import Faq

def show_landingpage(request):
    data_faq = Faq.objects.all()
    context = {
        # 'faq' : data_faq,
    }
    return render(request, "index.html", context)

def get_faq(request):
    FAQ = Faq.objects.all()

    return HttpResponse(serializers.serialize("json", FAQ), content_type="application/json")