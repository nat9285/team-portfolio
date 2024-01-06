from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la Categoría')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Proyecto')
    description = models.TextField(verbose_name='Descripción del Proyecto')
    start_date = models.DateField(verbose_name='Fecha de Inicio')
    categories = models.ManyToManyField(Category, verbose_name='Categorías del Proyecto', blank=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre de la persona')
    titles = models.CharField(max_length=100, verbose_name='Títulos de la persona', default="")
    biography = models.TextField(verbose_name='Biografía breve de la persona')

    def __str__(self):
        return self.name
