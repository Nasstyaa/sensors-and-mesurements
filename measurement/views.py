from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer, MeasurementsSerializer
from measurement.models import Sensor, Measurement


# Create your views here.


# Создать датчик. Указываются название и описание датчика. Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание
class SensorAPIList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


# Изменить датчик. Указываются название и описание. Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.
class SensorAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    # def patch(self, request, pk):
    #     sensor = Sensor.objects.get(pk=pk)
    #     serializer = SensorDetailSerializer(sensor, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #
    #     return Response(serializer.data)

# Добавить измерение. Указываются ID датчика и температура.
class MeasurementAPIList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer

    def get(self, request, pk):
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

# class SensorAPIDetailView(RetrieveUpdateDestroyAPIView):
#   queryset = Sensor.objects.all()
#   serializer_class = SensorDetailSerializer


# class SensorView(APIView):
#   def get(self, request):
#     sensors = Sensor.objects.all()
#     serializer = SensorSerializer(sensors, many=True)
#     return Response({'sensors': serializer.data})
