# Generated by Django 4.0.1 on 2023-07-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_accounttransation_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
