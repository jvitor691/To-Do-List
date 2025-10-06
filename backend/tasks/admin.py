from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'status']
    list_filter = ['status']
    search_fields = ['titulo', 'descricao']
    list_editable = ['status']
    ordering = ['-id']
