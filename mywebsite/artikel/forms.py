from django import forms
from django.forms import ModelForm

from .models import ModelArtikel

class FormArtikel(forms.ModelForm):
    class Meta:
        model = ModelArtikel
        fields = [
            'judul',
            'kategori',
            'body',
            'penulis',
            'image',
        ]

