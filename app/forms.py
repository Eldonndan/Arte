from django import forms
from . models import Obra

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre', 'dimensiones', 'destacada', 'fecha', 'descripcion', 'imagen', 'administradores', 'artistas', 'categorias', 'tipo_obra']