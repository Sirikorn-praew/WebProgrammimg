from django.db import models
from django.utils import timezone

class Task(models.Model):
    title = models.CharField(max_length=255)
    checkbox = models.BooleanField(default=False)
    # description = models.TextField()
    duedate = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    created_at = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d %H:%M:%S"))
    involved = models.ForeignKey('User', on_delete=models.SET_NULL, null= True, related_name='Involved')

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    # class Meta:
    #         full_name = ['first_name', 'last_name']

