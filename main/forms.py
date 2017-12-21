#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from main.models import *

class SearchForm(forms.Form):
    usuarioId = forms.IntegerField(label='Id del usuario', widget=forms.TextInput, required=True)