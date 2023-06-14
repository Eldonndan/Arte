from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'index.html', context)

def admin(request):
    context={}
    return render(request, 'admin.html', context)

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