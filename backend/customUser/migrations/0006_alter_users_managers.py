# Generated by Django 5.0.6 on 2024-05-22 11:43

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0005_users_is_admin'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='users',
            managers=[
                ('bishal', django.db.models.manager.Manager()),
            ],
        ),
    ]
