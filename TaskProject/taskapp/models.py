from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    # description = models.TextField()
    # created_at = models.DateField(auto_now_add=True)
    # last_update = models.DateTimeField(auto_now_add=True) 