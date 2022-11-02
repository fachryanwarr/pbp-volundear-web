from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from landingpage.models import Faq
from landingpage.models import Feedback
from django.views.decorators.csrf import csrf_exempt

def show_landingpage(request):
    context = {
    }
    return render(request, "index.html", context)

def get_faq(request):
    FAQ = Faq.objects.all()

    return HttpResponse(serializers.serialize("json", FAQ), content_type="application/json")

@csrf_exempt
def new_feedback(request):
    if request.method == "POST":
        nama = request.POST.get('name')
        pesan_feedback = request.POST.get('feedback')
        
        feedback = Feedback.objects.create(nama=nama, pesan_feedback=pesan_feedback)

    context = {
         'fb' : feedback.nama,
         'pesan': feedback.pesan_feedback,
         'pk' : feedback.pk,
    }
   
    return JsonResponse(context)

def show_feedback(request):
    context = {

    }
    return render(request, "feedback.html", context)

def get_feedback(request):
    feedbacks = Feedback.objects.all()

    return HttpResponse(serializers.serialize("json", feedbacks), content_type="application/json")