from rest_framework import serializers
from .models import *

class AnsiedadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ansiedad
        fields = '__all__'

class DatospersonalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datospersonales
        fields = '__all__'

class PsicosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Psicosis
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
