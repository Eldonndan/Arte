from django.shortcuts import render
from . models import Artista

# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context)

def administrador(request):
    context={}
    return render(request, 'administrador.html', context)

def agregarO(request):
    context={}
    return render(request, 'agregarO.html', context)

def formulario(request):
    context={}
    return render(request, 'formulario.html', context)

def galeria(request):
    context={}
    return render(request, 'galeria.html', context)

def loginAD(request):
    context={}
    return render(request, 'loginAD.html', context)

def loginAR(request):
    context={}
    return render(request, 'loginAR.html', context)

def obra1(request):
    context={}
    return render(request, 'obra1.html', context)

def obra2(request):
    context={}
    return render(request, 'obra2.html', context)

def obra3(request):
    context={}
    return render(request, 'obra3.html', context)

def obra4(request):
    context={}
    return render(request, 'obra4.html', context)

def TipoUsuario(request):
    context={}
    return render(request, 'TipoUsuario.html', context)

def registro(request):
    if request.method == 'POST':
        # procesar la solicitud POST
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("email")
        telefono = request.POST.get("telefono")
        contraseña = request.POST.get("password")
        obj = Artista.objects.create(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            telefono=telefono,
            contraseña=contraseña,
        )
        obj.save()
        context = {"mensaje": "Artista Ingresado Exitosamente!!!!!"}
        return render(request, "r.html", context)
    else:
        # si no es una solicitud POST, renderizar la plantilla de registro
        return render(request, "r.html")


def obra(request):
    if request.method == 'POST':
        # procesar la solicitud POST
        nombre = request.POST.get("nombre")
        dimensiones = request.POST.get("dimensiones")
        destacada = request.POST.get("destacada")
        fecha = request.POST.get("fecha")
        descripcion = request.POST.get("descripcion")
        imangen = request.POST.get("imagen")
        obj = Obra.objects.create(
            nombre=nombre,
            dimensiones=dimensiones,
            destacada=destacada,
            fecha=fecha,
            descripcion=descripcion,
            imangen=imagen,
        )
        obj.save()
        context = {"mensaje": "Obra Ingresada Exitosamente!!!!!"}
        return render(request, "Obra.html", context)
    else:
        # si no es una solicitud POST, renderizar la plantilla de registro
        return render(request, "Obra.html")




