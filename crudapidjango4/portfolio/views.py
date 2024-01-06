from .models import Project, Page
from rest_framework import viewsets
from .serializers import  ProjectAPISerializer,PageSerializer
from rest_framework.generics import RetrieveAPIView

# Create your views here.

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectAPISerializer

class ProjectDetail(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectAPISerializer
