from django.contrib import admin
from .models import Administrador, Artista, TipoObra, Duda, Obra, Categoria, RelacionArtistaObra, RelacionArtistaDuda, RelacionCategoriaObra

admin.site.register(Administrador)
admin.site.register(Artista)
admin.site.register(TipoObra)
admin.site.register(Duda)
admin.site.register(Obra)
admin.site.register(Categoria)
admin.site.register(RelacionArtistaObra)
admin.site.register(RelacionArtistaDuda)
admin.site.register(RelacionCategoriaObra)