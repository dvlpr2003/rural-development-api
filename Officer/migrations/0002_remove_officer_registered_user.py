# Generated by Django 5.0 on 2024-03-22 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Officer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='registered_user',
        ),
    ]
