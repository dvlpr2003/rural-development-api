# Generated by Django 5.0 on 2024-03-24 09:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complaint', '0001_initial'),
        ('signup', '0008_signup_officer'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='complaint',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Complaint.complaints'),
        ),
    ]