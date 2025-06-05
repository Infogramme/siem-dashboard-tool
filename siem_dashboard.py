# siem_dashboard_tool.py
"""
SIEM Dashboard Tool - Mini ELK Stack Clone for Security Event Monitoring
"""
from flask import Flask, render_template, jsonify, request
import random
import datetime

app = Flask(__name__)

# Simulated event logs
event_logs = [
    {"timestamp": str(datetime.datetime.now()), "source": "Firewall", "event": "Port scan detected", "severity": "High"},
    {"timestamp": str(datetime.datetime.now()), "source": "IDS", "event": "SQL Injection attempt", "severity": "Critical"},
    {"timestamp": str(datetime.datetime.now()), "source": "Auth", "event": "Failed login", "severity": "Medium"},
]

@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/api/logs")
def get_logs():
    return jsonify(event_logs)

@app.route("/api/add_log", methods=["POST"])
def add_log():
    new_log = request.json
    new_log["timestamp"] = str(datetime.datetime.now())
    event_logs.append(new_log)
    return jsonify({"status": "success"}), 201

if __name__ == "__main__":
    app.run(debug=True)

