from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class State(models.Model):
  name = models.CharField(verbose_name='Nombre', max_length=50)
  description = models.TextField(verbose_name='Descripcion')
  
  class Meta:
    verbose_name_plural = 'Estados'
    
  def __str__(self):
    return self.name

class Project(models.Model):
  name = models.CharField(verbose_name='Nombre', max_length=100)
  user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
  
  class Meta:
    verbose_name_plural = 'Proyectos'
  
  def __str__(self):
    return self.name

class Task(models.Model):
  title = models.CharField(verbose_name='Titulo', max_length=100)
  description = models.TextField(verbose_name='Descripcion')
  project = models.ForeignKey(Project, verbose_name=('Proyecto'), on_delete=models.CASCADE)
  due_date = models.DateField(verbose_name='Fecha de vencimiento')
  state = models.ForeignKey(State, verbose_name=('Estado'), on_delete=models.CASCADE, default=1)
  
  class Meta:
    verbose_name_plural = 'Tareas'
  
  def __str__(self):
    return self.title