from django.db import models
from django.conf import settings


class SensorData(models.Model):
    device_name = models.CharField(max_length=50)
    sol_temperature = models.FloatField()
    ec = models.FloatField()
    ph = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""SensorData
        device_name={self.device_name},
        sol_temperature={self.sol_temperature}, 
        ec={self.ec}, 
        ph={self.ph}, 
        temperature={self.temperature}, 
        humidity={self.humidity}, 
        timestamp={self.timestamp.strftime(settings.DATETIME_FORMAT)}"""
