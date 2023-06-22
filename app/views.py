from . models import Artista
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context)

def administrador(request):
    context={}
    return render(request, 'administrador.html', context)

def agregarO(request):
    return render(request, 'agregarO.html')

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

def login_view(request):
    if request.method == 'POST':
        try:
            detalleArtista=Artista.objects.get(correo=request.POST['email'], contraseña=request.POST['password'])
            print("Artista=",detalleArtista)
            request.session['correo']=detalleArtista.correo
            return render(request, 'agregarO.html')
        except Artista.DoesNotExist as e:
            messages.success(request, 'Nombre de usuario o Password no es correcto...!')
    return render(request, 'loginAR.html')

