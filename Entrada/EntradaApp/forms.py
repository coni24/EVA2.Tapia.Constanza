from django import forms
from EntradaApp.models import Entrada

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'