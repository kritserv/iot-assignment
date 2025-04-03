from rest_framework import serializers
from .models import SensorData

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'

class SensorSerializerWithOutlier(serializers.ModelSerializer):
    temperature_outlier = serializers.BooleanField()
    humidity_outlier = serializers.BooleanField()
    air_quality_outlier = serializers.BooleanField()

    class Meta:
        model = SensorData
        fields = '__all__'
