# Generated by Django 5.0.6 on 2024-05-21 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='fname',
            field=models.CharField(default='Bishal Phuyal', max_length=50),
            preserve_default=False,
        ),
    ]