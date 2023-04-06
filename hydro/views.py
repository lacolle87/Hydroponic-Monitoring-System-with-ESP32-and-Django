from .models import SensorData
from django.shortcuts import render
from django.http import JsonResponse
from . import mqtt_client
import time


def index(request):
    return render(request, 'hydro/index.html')


def get_latest_data(request):
    time.sleep(1)
    latest_data = SensorData.objects.order_by('-timestamp').first()
    data = {
        'device_name': latest_data.device_name,
        'sol_temperature': latest_data.sol_temperature,
        'ec': latest_data.ec,
        'ph': latest_data.ph,
        'temperature': latest_data.temperature,
        'humidity': latest_data.humidity,
        'timestamp': latest_data.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    }
    return JsonResponse(data)


mqtt_client.mqtt_client()
