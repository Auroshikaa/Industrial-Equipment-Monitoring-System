# Industrial Equipment Monitoring System

A multi-machine industrial monitoring platform that simulates real-time equipment telemetry, processes incoming machine data through a backend API, stores historical readings in a database, and visualizes equipment health through a real-time dashboard.

This project was built to simulate predictive maintenance workflows commonly used in manufacturing, industrial automation, aerospace systems, and defense asset monitoring environments.

---

## Project Overview

Industrial facilities often rely on continuous telemetry monitoring to detect abnormal equipment behavior before failures occur.

This system simulates multiple industrial machines generating telemetry data such as:

- Temperature
- Vibration
- Machine health status
- Failure conditions
- Historical operational trends

The platform monitors multiple machine types simultaneously and detects abnormal operating conditions through automated alerting logic.

---

## System Architecture

```text
Telemetry Simulator
        ↓
Flask API Backend
        ↓
SQLite Database
        ↓
Streamlit Dashboard
```

---

## Core Features

### Multi-Machine Telemetry Simulation
Simulates multiple industrial assets simultaneously:

- MOTOR_01
- MOTOR_02
- CONVEYOR_01
- COOLING_FAN_01

Each machine includes:

- Unique temperature thresholds
- Unique vibration thresholds
- Different operating profiles
- Different failure probabilities

---

### Fault Injection & Anomaly Simulation

The simulator dynamically generates:

- Normal operating states
- Warning conditions
- Critical failures

Simulated failures include:

- Overheating
- Excessive vibration
- Abnormal operating conditions

This helps mimic real-world predictive maintenance environments.

---

### API-Based Data Ingestion

A Flask backend receives telemetry using HTTP POST requests and processes incoming machine readings before storing them.

Example endpoint:

`/readings`

This architecture keeps telemetry generation decoupled from storage and visualization layers.

---

### Persistent Historical Storage

SQLite stores all telemetry readings for:

- Historical trend analysis
- Failure investigation
- Operational debugging
- Future predictive modeling opportunities

Stored fields include:

- machine_id
- machine_type
- timestamp
- temperature
- vibration
- status

---

### Real-Time Monitoring Dashboard

A Streamlit dashboard provides:

- Machine selection dropdown
- Real-time KPI monitoring
- Temperature trend visualization
- Vibration trend visualization
- Critical alert notifications
- Historical telemetry tables

---

## Dashboard Preview

### Main Dashboard
![Dashboard Overview](images/dashboard-overview.png)

---

### Trend Monitoring
![Trend Charts](images/trends.png)

---

### Critical Alert Example
![Critical Alert](images/critical-alert.png)

---

## Tech Stack

- Python
- Flask
- SQLite
- Streamlit
- Pandas
- Requests

---

## Project Structure

```text
industrial-equipment-monitoring-system/
│
├── telemetry_simulator.py
├── backend.py
├── database.py
├── dashboard.py
├── images/
├── README.md
└── .gitignore
```

---

## How to Run Locally

### Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/Industrial-Equipment-Monitoring-System.git
cd Industrial-Equipment-Monitoring-System
```

---

### Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install dependencies

```bash
pip install flask requests streamlit pandas streamlit-autorefresh
```

---

## Start Backend API

```bash
python backend.py
```

---

## Start Telemetry Simulator

```bash
python telemetry_simulator.py
```

---

## Launch Dashboard

```bash
streamlit run dashboard.py
```

---

## Future Improvements

Potential future upgrades:

- MQTT integration
- Cloud deployment (AWS/Azure)
- Real sensor integration
- Machine learning anomaly prediction
- Maintenance ticket automation
- Authentication/user roles

---

## Why I Built This

I wanted to build a project that combined:

- Systems engineering
- Backend development
- Data pipelines
- Reliability monitoring
- Industrial automation concepts

This project helped me better understand how telemetry systems operate in industrial, aerospace, and defense environments.
