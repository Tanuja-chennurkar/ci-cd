from flask import Flask, render_template, jsonify
import os
import socket

app = Flask(__name__)

# App version (used for UI + CI/CD demo)
APP_VERSION = "v2"
AUTO_REFRESH_SECONDS = 5 

def runtime_info():
    return {
        "pod_name": os.getenv("POD_NAME", "Unknown"),
        "node_name": os.getenv("NODE_NAME", "Unknown"),
        "image_name": os.getenv("IMAGE_NAME", "Unknown"),
        "version": APP_VERSION
    }

# --------------------
# UI Route
# --------------------
@app.route("/")
def index():
    info = runtime_info()
    return render_template(
        "index.html",
        pod_name=info["pod_name"],
        node_name=info["node_name"],
        image_name=info["image_name"],
        version=info["version"]
    )

# --------------------
# Auto-refresh API (UI polls this)
# --------------------
@app.route("/api/info")
def api_info():
    return jsonify(runtime_info()), 200

# --------------------
# Liveness Probe
# --------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "service": "flask-app",
        "node": socket.gethostname()
    }), 200

# --------------------
# Readiness Probe
# --------------------
@app.route("/ready")
def ready():
    return jsonify({
        "ready": True
    }), 200

# --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
