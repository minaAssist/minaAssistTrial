# Generated by Django 4.0.1 on 2023-08-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_alter_ticketrequest_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='address',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='district',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='state',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
