# Generated by Django 5.0 on 2024-04-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complaint', '0003_complaints_complaintimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='Accepted',
            field=models.BooleanField(default=False),
        ),
    ]
