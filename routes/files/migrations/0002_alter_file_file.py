# Generated by Django 3.2.9 on 2021-11-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.BinaryField(),
        ),
    ]
