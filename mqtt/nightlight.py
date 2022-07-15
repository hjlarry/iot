import time
import json

from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed
from paho.mqtt.client import Client

CounterFitConnection.init('127.0.0.1', 5000)

light_sensor = GroveLightSensor(0)
led = GroveLed(5)

id = 'a1043dc4-d663-4890-a919-3fb9ed851fff'
client_tele_topic = id + '/telemetry'
client_name = id + '-nightlight_client'

mqtt_client = Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()
print("MQTT connected!")

while True:
    light = light_sensor.light
    data = json.dumps({'light': light})
    print('sending telemetry ', data)
    mqtt_client.publish(client_tele_topic, data)
    time.sleep(5)
