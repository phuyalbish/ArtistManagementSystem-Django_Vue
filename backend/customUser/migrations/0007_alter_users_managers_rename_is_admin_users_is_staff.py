# Generated by Django 5.0.6 on 2024-05-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0006_alter_users_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='users',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]