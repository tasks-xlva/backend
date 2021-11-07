from django.db import models
from routes.groups.models import Group


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True)
    group = models.ForeignKey(Group, related_name="subjects", on_delete=models.CASCADE)
