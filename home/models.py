from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


    class Meta():
        ordering = ['complete']   

