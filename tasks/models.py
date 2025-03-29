from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nova'),
        ('in_progress', 'Em andamento'),
        ('completed', 'Concluída'),
        ('cancelled', 'Cancelada'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True, null=True)
    deadline = models.DateField()
    completion_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title