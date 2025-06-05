# siem_dashboard_tool.py
"""
SIEM Dashboard Tool - Mini ELK Stack Clone for Security Event Monitoring
"""
from flask import Flask, render_template, jsonify, request
import random
import datetime
import threading
import time
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Simulated event logs
event_logs = [
    {"timestamp": str(datetime.datetime.now()), "source": "Firewall", "event": "Port scan detected", "severity": "High"},
    {"timestamp": str(datetime.datetime.now()), "source": "IDS", "event": "SQL Injection attempt", "severity": "Critical"},
    {"timestamp": str(datetime.datetime.now()), "source": "Auth", "event": "Failed login", "severity": "Medium"},
]

# Threat categories for enrichment
threat_categories = {
    "Port scan detected": "Reconnaissance",
    "SQL Injection attempt": "Web Application Attack",
    "Failed login": "Brute Force Attack",
    "Cross-Site Scripting detected": "Web Application Attack",
    "DDoS detected": "Network Flood Attack"
}

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

@app.route("/api/stats")
def get_stats():
    stats = {}
    for log in event_logs:
        category = threat_categories.get(log["event"], "Other")
        stats[category] = stats.get(category, 0) + 1
    return jsonify(stats)

# Simulate log injection (for testing)
def simulate_events():
    sample_events = [
        {"source": "WAF", "event": "Cross-Site Scripting detected", "severity": "High"},
        {"source": "Firewall", "event": "DDoS detected", "severity": "Critical"}
    ]
    while True:
        time.sleep(10)
        log = random.choice(sample_events)
        log["timestamp"] = str(datetime.datetime.now())
        event_logs.append(log)

if __name__ == "__main__":
    os.makedirs("templates", exist_ok=True)
    with open("templates/dashboard.html", "w") as f:
        f.write("""
<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <title>SIEM Dashboard</title>
    <script src=\"https://cdn.jsdelivr.net/npm/chart.js\"></script>
</head>
<body>
    <h1>SIEM Dashboard</h1>
    <h2>Live Events</h2>
    <ul id=\"event-list\"></ul>

    <h2>Threat Statistics</h2>
    <canvas id=\"threatChart\" width=\"600\" height=\"400\"></canvas>

    <script>
        async function fetchLogs() {
            const response = await fetch('/api/logs');
            const data = await response.json();
            const list = document.getElementById('event-list');
            list.innerHTML = '';
            data.forEach(log => {
                const item = document.createElement('li');
                item.textContent = `${log.timestamp} | ${log.source} | ${log.event} | ${log.severity}`;
                list.appendChild(item);
            });
        }

        async function fetchStats() {
            const response = await fetch('/api/stats');
            const data = await response.json();
            const ctx = document.getElementById('threatChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: Object.keys(data),
                    datasets: [{
                        label: 'Threat Count',
                        data: Object.values(data),
                        backgroundColor: 'rgba(255, 99, 132, 0.5)'
                    }]
                }
            });
        }

        setInterval(() => {
            fetchLogs();
            fetchStats();
        }, 10000);

        fetchLogs();
        fetchStats();
    </script>
</body>
</html>
""")
    threading.Thread(target=simulate_events, daemon=True).start()
    app.run(debug=True)
