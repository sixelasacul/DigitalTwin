from paho.mqtt.client import Client
from datetime import datetime, timezone

from config import config

mqtt = config['mqtt']


class MQTT:
    def __init__(self):
        self.mqtt_client = Client(mqtt['client_id'])
        self.mqtt_client.username_pw_set("admin", "admin")
        self.mqtt_client.connect(mqtt['host'], mqtt['port'], mqtt['keep_alive'])

    def format_to_json(self, room, temperature):
        json_body = {
            "room": room,
            "source": "modbus",
            "time": datetime.now(timezone.utc).astimezone().isoformat(),
            "value": temperature
        }
        return json_body

    def publish_to_topic(self, temperature_per_room):
        for room in temperature_per_room:
            json_body = self.format_to_json(room, temperature_per_room[room])
            print("Sending to mqtt : %s" % json_body)
            self.mqtt_client.publish(mqtt['table'], str(json_body))
