# Generated by Django 3.2.9 on 2021-11-13 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('ADMIN', 'Администратор'), ('EDITOR', 'Редактор'), ('MEMBER', 'Участник')], max_length=15)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='groups.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
