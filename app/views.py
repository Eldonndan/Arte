from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from app.models import Administrador,Artista,Tecnica,Obra, ObraFav
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import TecnicaForm
from django.db.models import Q

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

def artistas(request):
    context={}
    return render(request, 'artistas.html', context)




def crear(request):
    if request.method != "POST":
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, 'registro.html', context)
    else:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        contraseña = request.POST["password"]
        obj1 = Artista.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            contraseña=contraseña,
        )
        obj = User.objects.create_user(
            username=email,
            password=contraseña,
            first_name=nombre,
            last_name=apellido
        )
        obj1.save()
        obj.save()
        
        users = User.objects.all()
        context = {"mensaje": "Artista Ingresado Exitosamente!!!!!",
            'users': users
        }
        return redirect('http://127.0.0.1:8000/login')

    
@login_required
def menu(request):
    user = request.user
    return render(request, 'menu.html', {'user': user})
    
def logout_view(request):
    logout(request)
    return redirect('login')

def inserta_tecnica(request):
    if request.method == "POST":
        form = TecnicaForm(request.POST)
        if form.is_valid():
            form.save()
            form=TecnicaForm()
            msg='Tecnica ingresado correctamente'
            context={"form":form,'msg':msg}
            return render(request,'crud/agregarT.html',context)
    else:
        form = TecnicaForm()
        context={"form":form}
        return render(request,'crud/agregarT.html',context)
    
def crud_tecnica(request):
	tecnicas=Tecnica.objects.all()
	context={"tecnicas":tecnicas}
	return render(request,'crud/crudtec.html',context)

def borra_tecnica(request,pk):
    try:
        tecnica=Tecnica.objects.get(id_tecnica=pk)
        tecnica.delete()
        tecnicas=Tecnica.objects.all()
        context={'tecnicas':tecnicas}
        return render(request,'crud/crudtec.html',context)
    except:
        mensaje='Tecnica no Existe'    
        tecnicas=Tecnica.objects.all()
        context={'tecnicas':tecnicas,'mensaje':mensaje}
        return render(request,'crud/crudtec.html',context)    

def modifica_tecnica(request,pk):
    try:
        tecnica=Tecnica.objects.get(id_tecnica=pk)      
        if tecnica:
            if request.method == "POST":
                form = TecnicaForm(request.POST,instance=tecnica)
                form.save()
                tecnicas=Tecnica.objects.all()
                contexto={'tecnicas':tecnicas}    
                return render(request,'crud/crudtec.html',contexto)
            else:
                form = TecnicaForm(instance=tecnica) 
                contexto={'form':form,'tecnica':tecnica}
                return render(request,'crud/modifica_tecnica.html',contexto)    
    except:
        contexto={'mensaje','Error - Tecnica no existe'}
        return render(request,'crud/crudtec.html',contexto)


@login_required
def crud(request):
    obras=Obra.objects.all()
    if "usuario" not in request.session:
        request.session["usuario"]=request.user.username
        usuario=request.session["usuario"]
    else:
        usuario=request.session["usuario"]    
    context={"obras":obras,"usuario":usuario}
    return render(request,'crud/crud.html',context)

def inserta_obra(request):
    if request.method != "POST":
        tecnicas=Tecnica.objects.all()
        context={"tecnicas":tecnicas}
        return render(request,'crud/agregarO.html',context)
    else:
        artista = Artista.objects.get(email=request.user.username)
        tecnicas=Tecnica.objects.all()
        titulo=request.POST["titulo"]
        dimensiones=request.POST["dimensiones"]
        fecha=request.POST["fecha"]
        tecnica=request.POST["tecnica"]
        descripcion=request.POST["descripcion"]
        imagen=request.FILES["imagen"]
        if "destacada" in request.POST:
            destacada=1
        else:
            destacada=0
        objTecnica=Tecnica.objects.get(id_tecnica=tecnica)
        obj=Obra.objects.create( titulo=titulo,
                                dimensiones=dimensiones,
                                fecha=fecha,
                                id_tecnica=objTecnica,
                                descripcion=descripcion,
                                imagen=imagen,
                                artista=artista,
                                destacada=destacada)
        obj.save() 
        context={"mensaje":'Obra Ingresada Exitosamente!'}
        return render(request,'crud/agregarO.html',context)

def borra_obra(request,pk):
    context={}
    try:
        obra=Obra.objects.get(id_obra=pk)
        obra.delete()
        mensaje='obra Eliminada Exitosamente'
        obras=Obra.objects.all()
        context={'obras':obras,'mensaje':mensaje}
        return render(request,'crud/crud.html',context)
    except:
        mensaje='Obra no Existe'    
        obras=Obra.objects.all()
        context={'obras':obras,'mensaje':mensaje}
        return render(request,'crud/crud.html',context)     

def busca_obra(request,pk):
    if pk!='':
        obra=Obra.objects.get(id_obra=pk)
        tecnicas=Tecnica.objects.all()
        context={'obra':obra,'tecnicas':tecnicas}
        if obra:
            return render(request,'crud/modifica_obra.html',context)
        else:
            context={'mensaje','Error - Obra no encontrado'}
            return render(request,'crud/crud.html',context)
        
def modifica_obra(request, pk):
    if request.method == "POST":
        obra = Obra.objects.get(id_obra=pk)
        artista = Artista.objects.get(email=request.user.username)
        tecnicas = Tecnica.objects.all()
        obra.titulo = request.POST["titulo"]
        obra.dimensiones = request.POST["dimensiones"]
        obra.fecha = request.POST["fecha"]
        obra.descripcion = request.POST["descripcion"]
        obra.id_tecnica = Tecnica.objects.get(id_tecnica=request.POST["tecnica"])
        if "destacada" in request.POST:
            obra.destacada=1
        else:
            obra.destacada=0

        # Verificar si se proporciona una nueva imagen
        imagen = request.FILES.get("imagen")
        if imagen:
            obra.imagen = imagen

        obra.save()  # Guardar los cambios en la obra existente

        obras = Obra.objects.all()
        context = {"obras": obras}
        return render(request, 'crud/crud.html', context)

    else:
        # Obtener la obra existente para mostrarla en el formulario
        obra = Obra.objects.get(id_obra=pk)
        tecnicas = Tecnica.objects.all()
        return render(request, 'crud/modifica_obra.html', {"obra": obra, "tecnicas": tecnicas})

def verfavorito(request):
    favoritos = ObraFav.objects.filter(user=request.user.username) 
    obra = Obra.objects.all()
    busqueda = request.GET.get("Buscar")
    if busqueda:
        obra = Obra.objects.filter(
            Q(titulo__icontains=busqueda) |
            Q(artista__icontains=busqueda)
        ).distinct()
    context = {
        "favoritos": favoritos, 
        "obra" : obra
    }
    return render(request, 'carrito/carrito.html', context)

def agregar_favorito(request, obra_id):
    user = User.objects.get()
    obras = Obra.objects.get(id_obra=obra_id)
    if ObraFav.objects.filter(user=user, obra=obras).exists():
        context={}
        return render(request, 'carrito/carrito.html', context)
    
    favor = ObraFav(user=user, obra=obras)
    favor.save()
    
    context = {}
    return render(request, 'carrito/carrito.html', context)