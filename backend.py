from flask import Flask, request, jsonify
from database import create_table, insert_reading

app = Flask(__name__)

create_table()


@app.route("/readings", methods=["POST"])
def receive_reading():
    data = request.get_json()

    insert_reading(data)

    print("\nStored telemetry:")from flask import Flask, request, jsonify
from database import create_table, insert_reading


app = Flask(__name__)

# Initialize the database table when the backend starts.
create_table()


@app.route("/readings", methods=["POST"])
def receive_reading():
    """Receive machine telemetry from the simulator and store it."""
    data = request.get_json()

    insert_reading(data)

    print("\nStored telemetry:")
    print(data)

    return jsonify({
        "message": "Telemetry stored successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
    print(data)

    return jsonify({
        "message": "Telemetry stored successfully"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)