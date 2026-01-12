import os
from flask import Flask, Response

app = Flask(__name__)

counter = 0

@app.route("/pingpong", methods=["GET"])
def pingpong():
    global counter
    response = f"pong {counter}"
    counter += 1
    return Response(response, mimetype="text/plain")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # default 8080
    app.run(host="0.0.0.0", port=port)
