from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet,ProjectDetail, PageViewSet

# Crea un enrutador y registra tu vista de conjunto
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project-list')  # 'projects' será la parte de la URL, puedes cambiarlo según tus preferencias
router.register(r'page', PageViewSet, basename='page-configuration')

# Configura las URLs de tu aplicación, incluyendo las generadas por el enrutador
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
]