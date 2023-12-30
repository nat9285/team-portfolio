from rest_framework import serializers
from .models import Project

#Los serializers son contenedores que nos permiten tomar tipos de datos complejos, convertirlos en datos nativos de python para después poderlos usar como JSON o XML.

class ProjectSerializer(serializers.ModelSerializer): #model ya que project es un modelo
    class Meta:
        model = Project #específicamos el modelo
        fields = '__all__' #serializar todos los campos