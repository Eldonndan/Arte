from django.db import models

# Create your models here.

class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=200, primary_key=True)
    telefono = models.IntegerField()
    contraseña = models.CharField(max_length=100)

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=200, primary_key=True)
    telefono = models.IntegerField()
    contraseña = models.CharField(max_length=100)

class Tecnica(models.Model):
    id_tecnica = models.AutoField(db_column='idTecnica',primary_key=True)
    tecnica = models.CharField(max_length=100, blank=False, null= False)

class Obra(models.Model):
    id_obra = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    dimensiones = models.IntegerField()
    destacada = models.IntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=400)
    imagen = models.ImageField(upload_to='obras/')
    id_tecnica = models.ForeignKey('Tecnica',on_delete=models.CASCADE, db_column='idTecnica')
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)