from django.db import models
from routes.groups.models import Group
from routes.files.models import File


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    group = models.ForeignKey(Group, related_name="subjects", on_delete=models.CASCADE)
    image = models.ForeignKey(File, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.group.number}, {self.name}"
