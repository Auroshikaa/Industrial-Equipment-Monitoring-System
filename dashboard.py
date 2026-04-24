import sqlite3
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

DATABASE_NAME = "monitoring.db"


def load_data() -> pd.DataFrame:
    connection = sqlite3.connect(DATABASE_NAME)

    query = """
    SELECT *
    FROM readings
    ORDER BY timestamp DESC
    """

    df = pd.read_sql_query(query, connection)
    connection.close()

    return df


st.set_page_config(
    page_title="Industrial Equipment Monitoring",
    layout="wide"
)

st_autorefresh(interval=5000, key="data_refresh")

st.title("Industrial Equipment Monitoring Dashboard")

df = load_data()

if df.empty:
    st.warning("No telemetry data found. Start the backend and simulator first.")
else:
    machine_options = sorted(df["machine_id"].unique())

    selected_machine = st.selectbox(
        "Select Machine",
        machine_options
    )

    filtered_df = df[df["machine_id"] == selected_machine].copy()

    latest = filtered_df.iloc[0]

    st.subheader("Current Machine Status")
    st.write(f"**Machine Type:** {latest['machine_type']}")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperature (°C)",
        latest["temperature"]
    )

    col2.metric(
        "Vibration",
        latest["vibration"]
    )

    col3.metric(
        "Status",
        latest["status"]
    )

    if latest["status"] == "Critical":
        st.error("CRITICAL ALERT: Immediate maintenance required.")
    elif latest["status"] == "Warning":
        st.warning("Warning: Monitor machine closely.")
    else:
        st.success("Machine operating normally.")

    st.subheader("Temperature Trend")
    st.line_chart(
        filtered_df.set_index("timestamp")["temperature"]
    )

    st.subheader("Vibration Trend")
    st.line_chart(
        filtered_df.set_index("timestamp")["vibration"]
    )

    st.subheader("Recent Readings")

    display_df = filtered_df.drop(columns=["id"])

    st.dataframe(
        display_df.head(20),
        use_container_width=True
    )