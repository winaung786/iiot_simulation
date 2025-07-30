import paho.mqtt.client as mqtt
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# List to store incoming sensor data (timestamp, raw JSON string)
data = []

def on_message(client, userdata, message):
    """Callback function triggered when an MQTT message is received."""
    payload = message.payload.decode("utf-8")
    # Append new data point
    data.append((datetime.now(), payload))
    # Limit the data list to the most recent 100 entries
    if len(data) > 100:
        data.pop(0)
    # Convert to pandas DataFrame
    df = pd.DataFrame(data, columns=["timestamp", "sensor_data"])
    # Parse JSON strings into numeric columns
    df["temperature"] = df["sensor_data"].apply(lambda x: eval(x)["temperature"])
    df["humidity"] = df["sensor_data"].apply(lambda x: eval(x)["humidity"])
    # Clear and update plot
    plt.clf()
    plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)")
    plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.draw()
    plt.pause(0.1)

# Create MQTT client and subscribe to the sensor data topic
client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor/data")
client.on_message = on_message

# Enable interactive plotting
plt.ion()
plt.figure()
# Start the MQTT client loop in a separate thread
client.loop_start()
# Keep the plot open
plt.show()
