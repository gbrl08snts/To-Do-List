from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.task_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'deadline': '2024-12-31',
            'status': 'new'
        }
        self.task = Task.objects.create(**self.task_data)

    def test_create_task(self):
        url = reverse('task-list')
        response = self.client.post(url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_single_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task_data['title'])

    def test_update_task(self):
        url = reverse('task-detail', args=[self.task.id])
        updated_data = {'title': 'Updated Task'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_create_task_missing_title(self):
        url = reverse('task-list')
        invalid_data = {
            'description': 'Test without title',
            'deadline': '2024-12-31'
        }
        response = self.client.post(url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Task.objects.count(), 1)