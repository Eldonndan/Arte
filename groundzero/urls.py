"""
URL configuration for groundzero project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('index/',views.index, name='index'),
    path('admin/', views.admin, name='admin'),
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
]
