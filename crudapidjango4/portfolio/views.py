from django.shortcuts import render

from rest_framework import generics

from portfolio.models import Project

from .serializers import ProjectSerializer

# Create your views here.

class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer