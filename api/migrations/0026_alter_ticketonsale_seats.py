# Generated by Django 4.0.1 on 2023-07-19 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_abstractedpassport_id_alter_attastation_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketonsale',
            name='seats',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
    ]
