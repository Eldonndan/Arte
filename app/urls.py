from django.urls import path
from . import views

    
    # otras URL aquí


urlpatterns = [
    path('index/', views.index, name='index'),
    path('artistas/', views.artistas, name='artistas'),
    path('administrador/', views.administrador, name='administrador'),
    path('agregarO/', views.agregarO, name='agregarO'),
    path('formulario/', views.formulario, name='formulario'),
    path('galeria/', views.galeria, name='galeria'),
    path('obra1/', views.obra1, name='obra1'),
    path('obra2/', views.obra2, name='obra2'),
    path('obra3/', views.obra3, name='obra3'),
    path('obra4/', views.obra4, name='obra4'),
    path('crear/', views.crear, name='crear'),
    path('menu/', views.menu, name='menu'),
    path('carrito/', views.verfavorito, name='carrito'),

    path('logout/', views.logout_view, name='logout'),
    path('agregar_favorito/<int:obra_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('crud_tecnica/', views.crud_tecnica, name='crud_tecnica'),
    path('inserta_tecnica', views.inserta_tecnica, name='inserta_tecnica'),
    path('borra_tecnica/<int:pk>',views.borra_tecnica,name='borra_tecnica'),
    path('modifica_tecnica/<int:pk>',views.modifica_tecnica,name='modifica_tecnica'),
    
    path('inserta_obra', views.inserta_obra, name='inserta_obra'),
    path('busca_obra/<str:pk>', views.busca_obra, name='busca_obra'),
    path('borra_obra/<str:pk>', views.borra_obra, name='borra_obra'),
    path('modifica_obra/<str:pk>',views.modifica_obra,name='modifica_obra'),

    path('crud/', views.crud, name='crud'),
]