# Generated by Django 5.0.6 on 2024-05-22 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_initial'),
        ('music', '0004_alter_music_album_alter_music_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.album'),
        ),
    ]
