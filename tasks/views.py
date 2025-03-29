# tasks/views.py
from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from .pagination import StandardResultsSetPagination  # Importe da nova localização

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = StandardResultsSetPagination  # Use a classe importada
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']