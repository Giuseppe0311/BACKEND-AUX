from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *

# Create your views here.
class AnsiedadViewSet(viewsets.ModelViewSet):
    queryset = Ansiedad.objects.all()
    serializer_class = AnsiedadSerializer
    permission_classes = [permissions.AllowAny]

class DatospersonalesViewSet(viewsets.ModelViewSet):
    queryset = Datospersonales.objects.all()
    serializer_class = DatospersonalesSerializer
    permission_classes = [permissions.AllowAny]

class PsicosisViewSet(viewsets.ModelViewSet):
    queryset = Psicosis.objects.all()
    serializer_class = PsicosisSerializer
    permission_classes = [permissions.AllowAny]

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [permissions.AllowAny]



