# Generated by Django 4.0.1 on 2023-07-28 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_accounttransation_title_ticketonsale_cabin_baggage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounttransation',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.agency'),
        ),
    ]
