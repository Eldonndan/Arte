from django.urls import path
from . import views
from .views import login_view

    
    # otras URL aquí


urlpatterns = [
    path('index/', views.index, name='index'),
    path('administrador/', views.administrador, name='administrador'),
    path('agregarO/', views.agregarO, name='agregarO'),
    path('formulario/', views.formulario, name='formulario'),
    path('galeria/', views.galeria, name='galeria'),
    path('loginAD/', views.loginAD, name='loginAD'),
    path('loginAR/', views.loginAR, name='loginAR'),
    path('obra1/', views.obra1, name='obra1'),
    path('obra2/', views.obra2, name='obra2'),
    path('obra3/', views.obra3, name='obra3'),
    path('obra4/', views.obra4, name='obra4'),
    path('TipoUsuario/', views.TipoUsuario, name='TipoUsuario'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
]