from django.core.management.base import BaseCommand
from tasks.models import Task
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Populates the database with sample tasks'

    def handle(self, *args, **options):
        statuses = ['new', 'in_progress', 'completed', 'cancelled']
        
        for i in range(1, 16):
            Task.objects.create(
                title=f'Tarefa {i}',
                description=f'Descrição da tarefa {i}',
                deadline=date.today() + timedelta(days=random.randint(-10, 30)),
                status=random.choice(statuses),
                completion_date=date.today() + timedelta(days=random.randint(-5, 5)) if random.choice([True, False]) else None
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 15 tasks'))