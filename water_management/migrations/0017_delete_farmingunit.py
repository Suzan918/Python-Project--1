# Generated by Django 4.2.15 on 2024-09-18 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('water_management', '0016_rename_unknown_reqno_farmingunit_reqno_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Farmingunit',
        ),
    ]
