from dataclasses import fields
from pyexpat import model
from django import forms
from django import forms
from artikel.models import Komentar

class CommentForm(forms.ModelForm):
    class Meta:
        model = Komentar
        fields = ('deskripsi',)

        widgets = {
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
        }