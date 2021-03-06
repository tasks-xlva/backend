import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from routes.users.models import User


class Group(models.Model):
    number = models.CharField(max_length=100)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.number


class Membership(models.Model):
    class Meta:
        unique_together = ["group", "user"]

    class Role(models.TextChoices):
        ADMIN = "ADMIN", _("Администратор")
        EDITOR = "EDITOR", _("Редактор")
        MEMBER = "MEMBER", _("Участник")

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="membership"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="membership")
    role = models.CharField(max_length=15, choices=Role.choices)

    def __str__(self):
        return f"{self.group.number}, {self.user.first_name} {self.user.last_name}, {self.role}"
