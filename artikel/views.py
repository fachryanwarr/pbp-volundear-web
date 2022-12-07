from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from artikel.models import *
from artikel.forms import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

def show_artikel(request):
    data = Artikel.objects.all()
    context = {
        'penulis': request.user,
        'artikel': data,
    }
    return render(request, "artikel.html", context)

def show_json(request):
    data = Artikel.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_comments_json(request):
    komentar_items = Komentar.objects.all()

    return HttpResponse(serializers.serialize("json", komentar_items), content_type="application/json")

@login_required(login_url='/auth/login/')
@csrf_exempt
def create_article_AJAX(request):
    if request.method == "POST":
        penulis = request.user
        judul = request.POST.get('judul')
        pembuka = request.POST.get('pembuka')
        isi = request.POST.get('isi')

        Artikel.objects.create(penulis=penulis,judul=judul, pembuka=pembuka, isi=isi)
    return JsonResponse({'error': False, 'msg':'Successful'})

@login_required(login_url='/auth/login/')
@csrf_exempt
def delete(request, id):
    if request.method == 'POST':
        data = get_object_or_404(Artikel, pk=id, penulis=request.user)
        data.delete()

        return JsonResponse({'error': False})

@login_required(login_url='/auth/login/')
def full_article(request,id):
    data = get_object_or_404(Artikel, pk=id)
    context = {
    'artikel': data,
    }
    return render(request, "fullArticle.html", context)

class AddCommentView(CreateView):
    model = Komentar
    form_class = CommentForm
    template_name = 'tambahKomentar.html'
    def form_valid(self, form):
        form.instance.artikel_id = self.kwargs['id']
        form.instance.penulis = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('artikel:show_artikel')
