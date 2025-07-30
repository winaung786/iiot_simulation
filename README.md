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
