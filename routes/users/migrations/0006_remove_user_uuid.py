# Generated by Django 3.2.9 on 2021-11-28 20:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uuid',
        ),
    ]
