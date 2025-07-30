import paho.mqtt.client as mqtt
import random
import time

# MQTT broker configuration
broker = "localhost"
port = 1883
topic = "sensor/data"

def simulate_sensor_data():
    """Continuously publish random temperature and humidity data to an MQTT topic."""
    while True:
        temperature = random.uniform(20.0, 25.0)
        humidity = random.uniform(30.0, 50.0)
        payload = f'{{"temperature": {temperature}, "humidity": {humidity}}}'
        client.publish(topic, payload)
        time.sleep(1)

# Create MQTT client and connect to the broker
client = mqtt.Client()
client.connect(broker, port)

# Start publishing sensor data
simulate_sensor_data()
