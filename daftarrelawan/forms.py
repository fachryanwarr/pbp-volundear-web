
from django import forms
from django.forms import fields
from daftarrelawan.models import DaftarRelawan


class DaftarRelawanForm(forms.ModelForm):
    class Meta:
        model = DaftarRelawan
        fields = {"keahlian", "mulai_periode", "akhir_periode" }
    widgets = {
        'keahlian': forms.CharField(),
        'mulai_periode': forms.DateField(),
        'akhir_periode': forms.DateField(),}
