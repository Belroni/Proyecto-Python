from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(
        verbose_name= 'Titulo',
        max_length=100
    )
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title + ' - by ' + self.user.username

class Inventario(models.Model):
    titulo = models.CharField(
        verbose_name='Titulo',
        max_length=100
    )
    descripcion = models.TextField(
        verbose_name = 'Descripción',
        blank= True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo + ' - ' + self.descripcion

# Create your models here.
