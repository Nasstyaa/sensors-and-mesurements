from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from measurement.serializers import SensorSerializer, MeasurementSerializer,  MeasurementsSerializer
from measurement.models import Sensor, Measurement

# Создать датчик. Указываются название и описание датчика. Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание
class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Изменить датчик. Указываются название и описание. Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.
class SensorAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

# Добавить измерение. Указываются ID датчика и температура.
class MeasurementAPIList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

