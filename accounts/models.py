from django.db import models
from contatos.models import contato
from django import forms


class FormCantato(forms.ModelForm):
    class Meta:
        model = contato
        exclude = ()
