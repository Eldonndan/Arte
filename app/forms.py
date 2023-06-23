from django import forms
from . models import Obra
from . models import Categoria
from django.forms import ModelForm

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre', 'dimensiones', 'destacada', 'fecha', 'descripcion', 'imagen', 'administradores', 'artistas', 'categorias', 'tipo_obra']


class CategoriaForm(ModelForm):
	class Meta:
		model = Categoria
		fields = ['nombre']
		labels = {'nombre':'Categoria'}