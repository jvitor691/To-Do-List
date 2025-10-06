from django.db import models
from django.core.validators import RegexValidator


class Task(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    ]
    
    titulo = models.TextField()
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pendente'
    )
    
    class Meta:
        db_table = 'tasks'
        ordering = ['-id']
    
    def __str__(self):
        return self.titulo
