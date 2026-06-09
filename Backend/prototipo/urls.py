"""
URL configuration for prototipo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from condominio import views

router = DefaultRouter()
router.register(r'sindicos', views.SindicoViewSet)
router.register(r'moradores', views.MoradorViewSet)
router.register(r'condominios', views.CondominioViewSet)
router.register(r'blocos', views.BlocoViewSet)
router.register(r'unidades', views.UnidadeViewSet)
router.register(r'saloes', views.SalaoViewSet)
router.register(r'quadras', views.QuadraViewSet)
router.register(r'veiculos', views.VeiculoViewSet)
router.register(r'reservas', views.ReservaViewSet)
router.register(r'ocorrencias', views.OcorrenciaViewSet)
router.register(r'faturas', views.FaturaFinanceiraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]