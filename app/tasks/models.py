from django.db import models
from app.subjects.models import Subject


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
