from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    air_quality = models.FloatField(blank=True, null=True)
