from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly define id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title