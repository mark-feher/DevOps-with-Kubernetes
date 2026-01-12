import time
import uuid
import threading
from datetime import datetime, timezone
from flask import Flask, jsonify

# Generate random string on startup
random_id = str(uuid.uuid4())

def current_timestamp():
    return (
        datetime.now(timezone.utc)
        .isoformat(timespec="milliseconds")
        .replace("+00:00", "Z")
    )

# Logging loop (runs in background thread)
def log_loop():
    while True:
        print(f"{current_timestamp()}: {random_id}", flush=True)
        time.sleep(5)

# Start logging thread
threading.Thread(target=log_loop, daemon=True).start()

# HTTP app
app = Flask(__name__)

@app.route("/status", methods=["GET"])
def status():
    return jsonify({
        "timestamp": current_timestamp(),
        "id": random_id
    })

if __name__ == "__main__":
    # Listen on all interfaces so Kubernetes can reach it
    app.run(host="0.0.0.0", port=8080)
