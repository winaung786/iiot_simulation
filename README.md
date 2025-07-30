# IIoT Sensor Network Simulation

## 📘 Project Overview

This project is part of **Lab 04: Conceptual Design of an IIoT Sensor Network**. It simulates real-time sensor data transmission using three Industrial Internet of Things (IIoT) communication protocols: **MQTT**, **CoAP**, and **OPC UA**. The simulation also includes a **real-time data visualization** script to display the collected sensor values (temperature and humidity) from the MQTT protocol.

---

## 📁 Project Structure


---

## 🧪 What Each File Does

- `mqtt_sensor_simulation.py`: Simulates sensor data (temperature, humidity) using MQTT protocol.
- `coap_sensor_simulation.py`: Simulates sensor data using CoAP protocol.
- `opcua_sensor_simulation.py`: Simulates sensor data using OPC UA protocol.
- `data_visualization.py`: Subscribes to MQTT sensor data and plots real-time graphs.
- `comparison_report.pdf`: A short report comparing MQTT, CoAP, and OPC UA.
- `visualizations/`: Contains PNG screenshots of the graphs and a demo video of the visualization.

---

## ⚙️ Requirements

Make sure you have **Python 3.x** and the following Python libraries installed:

```bash
pandas
numpy
paho-mqtt
aiocoap
asyncua
matplotlib

## ▶️ How to Run the Project

Follow these steps to run the sensor simulation and visualization:

---

### 🔹 1. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

---

### 🔹 2. Start the MQTT Broker

Open a new terminal and run:
```bash
mosquitto
```
Make sure Mosquitto is installed. Download: https://mosquitto.org/download

---

### 🔹 3. Run Sensor Simulations (Each in Separate Terminals)

**MQTT Simulation**
```bash
python mqtt_sensor_simulation.py
```

**CoAP Simulation**
```bash
python coap_sensor_simulation.py
```

**OPC UA Simulation**
```bash
python opcua_sensor_simulation.py
```

---

### 🔹 4. Run the Data Visualization Script

In a new terminal (with virtual environment activated):
```bash
python data_visualization.py
```

You will see a live plot showing Temperature and Humidity from the MQTT simulation.


