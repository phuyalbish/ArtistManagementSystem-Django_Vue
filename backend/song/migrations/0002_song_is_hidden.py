# Generated by Django 5.0.6 on 2024-05-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]