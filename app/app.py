
from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = {}

@app.route("/tasks", methods=["POST"])
def create_task():
    tenant = request.headers.get("X-Tenant-ID", "default")
    data = request.json
    tasks.setdefault(tenant, []).append(data)
    return jsonify({"status": "created", "tenant": tenant})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tenant = request.headers.get("X-Tenant-ID", "default")
    return jsonify(tasks.get(tenant, []))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
