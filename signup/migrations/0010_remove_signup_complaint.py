# Generated by Django 5.0 on 2024-03-24 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_signup_complaint'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='complaint',
        ),
    ]