# Generated by Django 4.2.15 on 2024-09-18 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_management', '0021_gardeningschedule_gnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gardeningschedule',
            name='status',
        ),
        migrations.AddField(
            model_name='gardeningschedule',
            name='category',
            field=models.CharField(choices=[('low', 'low'), ('moderate', 'moderate'), ('high', 'high')], default='low', max_length=50),
        ),
    ]
