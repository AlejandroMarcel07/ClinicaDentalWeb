from django.contrib import admin
from .models import TbExploracionclinica

class TbExploracionclinicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo')  # Campos a mostrar en la lista de administración
    search_fields = ('tipo',)  # Permite buscar por el tipo de exploración
    ordering = ('id',)  # Ordenar por ID

admin.site.register(TbExploracionclinica, TbExploracionclinicaAdmin)
