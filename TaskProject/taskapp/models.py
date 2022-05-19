from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    checkbox = models.BooleanField(default=False)
    # description = models.TextField()
    duedate = models.DateTimeField(auto_now_add=True) #, default=timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    created_at = models.DateTimeField(auto_now_add=True) #, default=timezone.now().strftime("%Y-%m-%d %H:%M:%S")
    involved = models.ManyToManyField(User, related_name='Involved')
    # involved = models.ForeignKey('User', on_delete=models.SET_NULL, null= True, related_name='Involved')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['checkbox']

# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=255)
#     task = models.ForeignKey(Task, on_delete=models.PROTECT)

#     def __str__(self) -> str:
#         return f'{self.first_name} {self.last_name}'

    # class Meta:
    #         full_name = ['first_name', 'last_name']

