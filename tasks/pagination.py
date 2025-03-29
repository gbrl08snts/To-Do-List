# tasks/pagination.py
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5  # 5 tarefas por página (requisito 1.1)
    page_size_query_param = 'page_size'
    max_page_size = 100