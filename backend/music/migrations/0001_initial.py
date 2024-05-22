# Generated by Django 5.0.6 on 2024-05-22 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img_src', models.CharField(max_length=100, null='default_album.png')),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('totallikes', models.IntegerField(default=0)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='album.album')),
                ('artist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]