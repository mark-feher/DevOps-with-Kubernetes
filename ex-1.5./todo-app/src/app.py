import os
from flask import Flask

app = Flask(__name__)

# Get the port from the environment, default to 3030
port = int(os.getenv("PORT", 3030))

@app.route("/")
def index():
    return "Nothing to see here yet"

if __name__ == "__main__":
    print(f"Server started on port {port}")
    app.run(host="0.0.0.0", port=port)
