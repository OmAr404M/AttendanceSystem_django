# Generated by Django 4.2 on 2023-05-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0008_studentextra_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='roll',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
