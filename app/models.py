from django.db import models

class Administrador(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    telefono = models.BigIntegerField()
    contraseña = models.CharField(max_length=300)

class Artista(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo =models.EmailField(unique=True)
    telefono = models.BigIntegerField()
    contraseña = models.CharField(max_length=300)

class TipoObra(models.Model):
    id_tipo = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)

class Duda(models.Model):
    id_duda = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='dudas/')
    administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)

class Obra(models.Model):
    id_obra = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=500)
    dimensiones = models.CharField(max_length=50)
    destacada = models.BooleanField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to='obras/')
    administradores = models.ManyToManyField(Administrador, related_name='obras_administradas')
    artistas = models.ManyToManyField(Artista, related_name='obras_creadas')
    categorias = models.ManyToManyField('Categoria')
    tipo_obra = models.ForeignKey(TipoObra, on_delete=models.CASCADE)

class Categoria(models.Model):
    id_cate = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    obras = models.ManyToManyField(Obra)

class RelacionArtistaObra(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)

class RelacionArtistaDuda(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    duda = models.ForeignKey(Duda, on_delete=models.CASCADE)

class RelacionCategoriaObra(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)