from django import forms
from . models import Tecnica

from django.forms import ModelForm

class TecnicaForm(ModelForm):
	class Meta:
		model=Tecnica
		fields = ['tecnica']
		labels = {'tecnica':'Tecnica'}