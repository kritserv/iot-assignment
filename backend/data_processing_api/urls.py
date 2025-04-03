from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.CreateSensor.as_view(), name='data'),
    path('processed/', views.CleanSensor.as_view(), name='process'),
    path('aggregated/', views.FetchSensorStatistics.as_view(), name='aggregated'),
]
