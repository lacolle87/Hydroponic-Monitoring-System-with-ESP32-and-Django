import json
import paho.mqtt.client as mqtt
from django.utils import timezone
from .models import SensorData

MQTT_SERVER = "192.168.1.87"
MQTT_PORT = 1883
MQTT_USERNAME = "doggo"
MQTT_PASSWORD = "doggo1987"
MQTT_TOPIC = "habanero1"


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    print("Received message: " + payload)
    try:
        data = json.loads(payload)
        device_name = str(data["device_name"])
        sol_temperature = float(data["sol_temperature"])
        ec = float(data["ec"])
        ph = float(data["ph"])
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        reading = SensorData.objects.create(device_name=device_name,
                                            sol_temperature=sol_temperature,
                                            ec=ec,
                                            ph=ph,
                                            temperature=temperature,
                                            humidity=humidity)
        reading.timestamp = timezone.now()
        reading.save()
        print(f"Saved {device_name} reading: " + str(reading))
    except (ValueError, KeyError):
        print("Invalid data received")


def mqtt_client():
    client = mqtt.Client()
    client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_SERVER, MQTT_PORT, 60)

    client.loop_start()
