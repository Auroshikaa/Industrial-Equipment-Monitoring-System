import sqlite3


DATABASE_NAME = "monitoring.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    """Create the telemetry table if it does not already exist."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id TEXT NOT NULL,
            machine_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL,
            vibration REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def insert_reading(reading: dict):
    """Store one machine telemetry reading."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO readings (
            machine_id,
            machine_type,
            timestamp,
            temperature,
            vibration,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        reading["machine_id"],
        reading["machine_type"],
        reading["timestamp"],
        reading["temperature"],
        reading["vibration"],
        reading["status"],
    ))

    connection.commit()
    connection.close()