import time
import json
from paho.mqtt.client import Client

id = 'a1043dc4-d663-4890-a919-3fb9ed851fff'
client_tele_topic = id + '/telemetry'
server_name = id + '-server'

mqtt_client = Client(server_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()
print("MQTT connected!")


def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)


mqtt_client.subscribe(client_tele_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)
