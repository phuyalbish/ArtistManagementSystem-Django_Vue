# Generated by Django 5.0.6 on 2024-05-27 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0009_alter_users_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='link',
            new_name='links',
        ),
    ]
