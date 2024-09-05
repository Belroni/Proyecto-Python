from django.forms import ModelForm
from .models import Task, Inventario

class TaskForm(ModelForm):
    class Meta:
        model= Task
        fields = ['title', 'description', 'important']

class InventarioForm(ModelForm):
    class Meta:
        model= Inventario
        fields = ['titulo', 'descripcion', 'activo']