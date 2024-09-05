from django.contrib import admin
from .models import Task, Inventario

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "created", )

# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(Inventario)