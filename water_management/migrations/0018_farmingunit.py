# Generated by Django 4.2.15 on 2024-09-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_management', '0017_delete_farmingunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reqno', models.CharField(default='UNKNOWN_REQNO', max_length=20, unique=True)),
                ('town', models.CharField(default='none', max_length=100)),
                ('no', models.PositiveIntegerField(default=0)),
                ('type', models.CharField(default='Farming units/enterprise', max_length=100)),
                ('district', models.CharField(default='none', max_length=100)),
                ('amount', models.PositiveIntegerField(default=0.0)),
            ],
        ),
    ]
