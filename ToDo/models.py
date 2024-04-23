from django.db import models
from django.utils import timezone

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    due_date = models.DateTimeField("Fecha Limite")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
    
    def is_due(self):
        return self.due_date <= timezone.now()
    