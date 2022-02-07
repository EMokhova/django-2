from django.urls import path

from measurement.views import SensorView, MeasurementView, SensorMeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorMeasurementView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
