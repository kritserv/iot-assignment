from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    air_quality = models.FloatField()
