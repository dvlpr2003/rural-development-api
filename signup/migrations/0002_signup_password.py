# Generated by Django 5.0 on 2024-03-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
