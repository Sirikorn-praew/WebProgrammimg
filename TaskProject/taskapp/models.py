from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    checkbox = models.CharField(max_length=255, default="")
    # description = models.TextField()
    # created_at = models.DateField()
    # last_update = models.DateTimeField(auto_now_add=True) 