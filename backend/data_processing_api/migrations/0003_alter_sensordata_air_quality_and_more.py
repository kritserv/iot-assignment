# Generated by Django 5.2 on 2025-04-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_processing_api', '0002_rename_ingestsensordata_sensordata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='air_quality',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensordata',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
