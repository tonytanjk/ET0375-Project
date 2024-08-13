# Automated Gardening System Dashboard

https://github.com/ET0735-DevOps-AIoT-AY2410/DCPE_2A_05_Group5/blob/Tony/Project_Video.mp4

## Table of Contents

- [System Overview](#system-overview)
- [Functional Requirements](#functional-requirements)
  - [Dashboard](#dashboard)
  - [pH Level](#ph-level)
  - [Temperature](#temperature)
  - [Humidity](#humidity)
  - [Light Intensity](#light-intensity)
  - [Electrical Conductivity (EC)](#electrical-conductivity-ec)
- [Non-Functional Requirements](#non-functional-requirements)
- [Software Architecture](#software-architecture)

## System Overview

The Automated Hydroponics Dashboard is a system designed to monitor and manage key environmental parameters essential for hydroponic farming. This dashboard provides real-time insights and control mechanisms to ensure optimal growth conditions for plants by tracking pH levels, temperature, humidity, light intensity, and electrical conductivity (EC).

### System Architecture

The system includes the following components:
- **Sensors**: DHT11, LDR, Measure pH levels, temperature, humidity, light intensity, and electrical conductivity.
- **Actuators**: DC Motor, LEDS , and servo motors for fan, UV light and dispensing solutions based on sensor data respectively.
- **Raspberry Pi**: Acts as the central processing unit, running a Flask server for frontend dashboard updates and backend data handling .
- **Dashboard**: A web-based interface for real-time monitoring and control, implemented using Flask and Socket.IO.

### Hardware

- Raspberry Pi Development Board
- Temperature Sensor
- Humidity Sensor
- Light Intensity Sensor
- pH Level Sensor
- EC Level Sensor
- Servo Motor
- DC Motors
- UV Light (LED)
- Fan
- LCD Screen
- Keypad

### Software

- Flask for backend API and server management
- Socket.IO for real-time data communication between server and clients
- Python for sensor data processing and main function of System
- jsDelivr Chart.js for graph generation
## Functional Requirements

### Dashboard

- **REQ-01**: Retrieve sensor data from Raspberry Pi.
- **REQ-02**: Dynamically update the dashboard with the latest sensor data.
- **REQ-03**: Provide visual warnings when temperature or pH levels are outside the acceptable range.

### pH Level

- **REQ-04**: Register pH levels input via a keypad.
- **REQ-05**: Display and upload pH data to the dashboard.

### Temperature

- **REQ-06**: Measure temperature using a sensor.
- **REQ-07**: Display temperature on an LCD and upload data to the dashboard.
- **REQ-08**: Detect when the temperature exceeds 25°C.
- **REQ-09**: Activate the fan if the temperature exceeds 25°C.

### Humidity

- **REQ-10**: Measure humidity using a sensor and upload the data to the dashboard.

### Light Intensity

- **REQ-11**: Measure light intensity using an LDR sensor.
- **REQ-12**: Display and upload light intensity data to the dashboard.
- **REQ-13**: Activate UV lights when light intensity falls below 4 lux.

### Electrical Conductivity (EC)

- **REQ-14**: Measure electrical conductivity levels.
- **REQ-15**: Display and upload EC data to the dashboard.
- **REQ-16**: Check if EC levels fall within the range of 1.0 - 2.5.
- **REQ-17**: Dispense a solution using a servo motor if EC levels are out of range.

## Non-Functional Requirements

- **REQ-18**: Display the dashboard on a mobile application.
- **REQ-19**: Show detailed pH levels history when clicked on the dashboard.
- **REQ-20**: Show detailed temperature history, including fan activation events.
- **REQ-21**: Show detailed humidity levels history.
- **REQ-22**: Show detailed light intensity history, including LED activation events.
- **REQ-23**: Show detailed EC levels history, including solution dispensing events.

## Software Architecture

The system software is divided into several layers:
- **Application Layer**: Manages the dashboard and user interaction.
- **Hardware Abstraction Layer (HAL)**: Interfaces with sensors and actuators.
- **Flask Server**: Handles data processing and communication between the hardware and the dashboard.
- **Socket.IO**: Facilitates real-time updates on the dashboard.

## Getting Started
1. Install Flask and Socket.IO on the Raspberry Pi.
2. Install Python dependencies:
   ```bash
   pip install flask flask-socketio
3. Deploy the provided Flask app for backend services and dashboard visualization.

### Prerequisites

- Raspberry Pi with a working installation of Raspbian OS.
- DHT11 Sensor (GPIO 21)
- Light Intensity Sensor (ADC Channel 0)
- Keypad or Actual pH sensor (GPIO: Row:6,20,19,3 Col: 12,5,6)
- LCD Display
- DC Motor (GPIO 23)
- Servo Motor (GPIO 26)
- LED (GPIO 24)
- Python 3.x installed on the Raspberry Pi.
- Flask and Socket.IO installed on the Raspberry Pi.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/automated-gardening-system.git
2. Install Python dependencies:
   ```bash
   pip install flask flask-socketio spidev psutil
3. Deploy the provided Flask app for backend services and dashboard visualization.

## Project Distribution
1. Wang HongXiang - Video editting, Ph level requirements, Ambient light intensity requirements, docs
2. Praha - Mobile application, web page, dashboard, API, Bug fixes, Web Sockets, docs
3. Tony - Ambient Temperature and Humidity, API, Bug fixes, Threading, docs, dockerfile
4. Keegan - Mobile application Graphs, EC levels requirements, Bug fixes, docs, docker
