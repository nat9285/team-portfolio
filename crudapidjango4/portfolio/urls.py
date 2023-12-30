#creamos éste archivo para cargar las direcciones de las vistas de nuestra app portfolio

from django.urls import path
from .views import ProjectList, ProjectDetail

urlpatterns = [
    path('proyectos/', ProjectList.as_view(), name='lista-proyectos'), #con as_view especifico que debe ser una vista
    path('proyectos/<int:pk>/', ProjectDetail.as_view(), name='detalle-proyecto'),
]