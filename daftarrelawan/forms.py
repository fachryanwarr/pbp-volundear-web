
from django import forms
from django.forms import fields
from daftarrelawan.models import DaftarRelawan

class DaftarRelawanForm(forms.Form):
        keahlian = forms.CharField()
        tanggal = forms.DateField()
        jam = forms.TimeField()


