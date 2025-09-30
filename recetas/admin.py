from django.contrib import admin
from .models import Receta

# Register your models here.

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha_creacion']
