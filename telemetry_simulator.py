import random
import time
import json
import requests
from datetime import datetime


API_URL = "http://127.0.0.1:5000/readings"

MACHINES = [
    {
        "machine_id": "MOTOR_01",
        "machine_type": "conveyor_motor",
        "normal_temp": (35.0, 45.0),
        "warning_temp": (46.0, 55.0),
        "critical_temp": (56.0, 70.0),
        "normal_vibration": (0.20, 0.50),
        "warning_vibration": (0.51, 0.80),
        "critical_vibration": (0.81, 1.20),
        "failure_chance": 0.08,
    },
    {
        "machine_id": "MOTOR_02",
        "machine_type": "pump_motor",
        "normal_temp": (38.0, 48.0),
        "warning_temp": (49.0, 58.0),
        "critical_temp": (59.0, 75.0),
        "normal_vibration": (0.25, 0.55),
        "warning_vibration": (0.56, 0.85),
        "critical_vibration": (0.86, 1.30),
        "failure_chance": 0.12,
    },
    {
        "machine_id": "CONVEYOR_01",
        "machine_type": "belt_conveyor",
        "normal_temp": (30.0, 42.0),
        "warning_temp": (43.0, 52.0),
        "critical_temp": (53.0, 65.0),
        "normal_vibration": (0.15, 0.45),
        "warning_vibration": (0.46, 0.75),
        "critical_vibration": (0.76, 1.10),
        "failure_chance": 0.10,
    },
    {
        "machine_id": "COOLING_FAN_01",
        "machine_type": "cooling_fan",
        "normal_temp": (28.0, 40.0),
        "warning_temp": (41.0, 50.0),
        "critical_temp": (51.0, 62.0),
        "normal_vibration": (0.10, 0.35),
        "warning_vibration": (0.36, 0.65),
        "critical_vibration": (0.66, 1.00),
        "failure_chance": 0.15,
    },
]


def choose_machine_state(machine: dict) -> str:
    """Choose the current machine state based on its failure profile."""
    roll = random.random()

    if roll < machine["failure_chance"]:
        return "critical"
    elif roll < machine["failure_chance"] + 0.20:
        return "warning"
    return "normal"


def generate_value(value_range: tuple[float, float]) -> float:
    return round(random.uniform(value_range[0], value_range[1]), 2)


def classify_status(machine: dict, temperature: float, vibration: float) -> str:
    """Classify machine health using machine-specific thresholds."""
    if (
        temperature >= machine["critical_temp"][0]
        or vibration >= machine["critical_vibration"][0]
    ):
        return "Critical"

    if (
        temperature >= machine["warning_temp"][0]
        or vibration >= machine["warning_vibration"][0]
    ):
        return "Warning"

    return "Normal"


def generate_reading(machine: dict) -> dict:
    """Generate one telemetry reading for a single machine."""
    state = choose_machine_state(machine)

    temperature = generate_value(machine[f"{state}_temp"])
    vibration = generate_value(machine[f"{state}_vibration"])
    status = classify_status(machine, temperature, vibration)

    return {
        "machine_id": machine["machine_id"],
        "machine_type": machine["machine_type"],
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "temperature": temperature,
        "vibration": vibration,
        "status": status,
    }


def send_reading(reading: dict) -> None:
    """Send telemetry to the backend API."""
    try:
        response = requests.post(API_URL, json=reading)

        print("Sent telemetry:")
        print(json.dumps(reading, indent=2))
        print("Server response:", response.json())
        print("-" * 40)

    except requests.exceptions.RequestException as error:
        print("Failed to send telemetry:", error)


def main() -> None:
    print("Starting industrial equipment telemetry simulator...\n")

    while True:
        for machine in MACHINES:
            reading = generate_reading(machine)
            send_reading(reading)

        time.sleep(5)


if __name__ == "__main__":
    main()