# Generated by Django 5.0 on 2024-03-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_remove_signup_otp_delete_onetimepassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='name',
        ),
        migrations.AddField(
            model_name='signup',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]
