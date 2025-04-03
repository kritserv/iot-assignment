from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from datetime import timedelta
from django.utils import timezone
from .models import SensorData
from .serializers import SensorSerializer
from .data_cleaner import remove_duplicated, fix_missing_values, remove_outliers
from .data_stat import get_statistics

class CreateSensor(generics.ListCreateAPIView):
    queryset = SensorData.objects.all()
    serializer_class = SensorSerializer

class CleanSensor(APIView):
    def get(self, request, format=None):
        df = pd.DataFrame.from_records(SensorData.objects.all().values())
        df = remove_duplicated(df)
        df = fix_missing_values(df)
        df = remove_outliers(df)
        serializer = SensorSerializer(df.to_dict('records'), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class FetchSensorStatistics(APIView):
    def get(self, request, format=None):
        hours = request.query_params.get('hours', 0)
        minutes = request.query_params.get('minutes', 0)

        time_delta = timedelta(hours=int(hours), minutes=int(minutes))
        start_date = timezone.now() - time_delta

        if start_date:
            queryset = SensorData.objects.filter(timestamp__gte=start_date)
        else:
            queryset = SensorData.objects.all()

        df = pd.DataFrame.from_records(queryset.values())
        if df.empty:
            return Response({'message': 'No data available'}, status=status.HTTP_204_NO_CONTENT)
        result = get_statistics(df)

        return Response(result, status=status.HTTP_200_OK)
