from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter()
router.register('Ansiedad', AnsiedadViewSet)
router.register('Datospersonales', DatospersonalesViewSet)
router.register('Psicosis', PsicosisViewSet)
router.register('Usuarios', UsuariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]