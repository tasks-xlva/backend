from django.db import models
from routes.subjects.models import Subject
from routes.files.models import File


class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="tasks")
    attachments = models.ManyToManyField(File, blank=True)

    def __str__(self):
        return f"{self.subject}, {self.name}"
