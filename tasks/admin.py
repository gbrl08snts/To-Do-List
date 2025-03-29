from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline')  # Campos visíveis na lista
    search_fields = ('title', 'description')        # Campos pesquisáveis

admin.site.register(Task, TaskAdmin)  # Registra com configurações customizadas