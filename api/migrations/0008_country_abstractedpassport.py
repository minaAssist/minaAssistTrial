# Generated by Django 4.0.1 on 2023-06-25 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_accounttransation_gross_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ailine_name', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AbstractedPassport',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name=uuid.uuid4)),
                ('given_name', models.CharField(blank=True, max_length=25, null=True)),
                ('surname', models.CharField(blank=True, max_length=20, null=True)),
                ('pass_number', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('pass_issue', models.DateField(blank=True, null=True)),
                ('pass_expiry', models.DateField(blank=True, null=True)),
                ('issue_place', models.CharField(blank=True, max_length=10, null=True)),
                ('sex', models.CharField(blank=True, max_length=5, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
