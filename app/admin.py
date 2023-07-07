from django.contrib import admin
from .models import Administrador, Artista, Tecnica, Obra

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Artista)
admin.site.register(Tecnica)
admin.site.register(Obra)
