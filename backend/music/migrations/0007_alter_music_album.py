# Generated by Django 5.0.6 on 2024-05-22 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_remove_album_totalsongs_album_is_deleted_and_more'),
        ('music', '0006_music_modified_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='album.album'),
        ),
    ]
