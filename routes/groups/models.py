from django.db import models


class Group(models.Model):
    number = models.CharField(max_length=10)
