from django.db import models

class webBranch(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre de la Rama')
    boolean = models.BooleanField(default=False, verbose_name='Curso hecho')

    def __str__(self):
        return self.name

class Classification(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre de la Categoría')
    webBranch = models.ForeignKey(webBranch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombre del Proyecto')
    description = models.TextField(verbose_name='Descripción del Proyecto')
    date = models.DateField(verbose_name='Fecha de Inicio')
    classification= models.ForeignKey(Classification, on_delete=models.CASCADE, verbose_name='Categoría del Proyecto')
    github = models.CharField(max_length=255, verbose_name='Dirección github', default=None)
    server = models.CharField(max_length=255, verbose_name='Dirección servidor', default=None)
    def __str__(self):
        return self.name