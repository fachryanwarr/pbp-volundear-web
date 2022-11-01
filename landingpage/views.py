from django.shortcuts import render

def show_landingpage(request):
    return render(request, "index.html")

# Create your views here.
