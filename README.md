# siem-dashboard-tool
This is a simple mini SIEM (Security Information and Event Management) dashboard tool inspired by the ELK Stack. It allows users to visualize and interact with simulated security logs in real time via a web interface built with Flask.
## Features
- Real-time display of simulated security logs (e.g., firewall, IDS, authentication events)
- API endpoint to fetch and add logs
- Web-based dashboard for visualization
- Can be extended to integrate with actual log sources or ELK components

## Installation
1. Clone the repository:
```bash
git clone https://github.com/infogramme/siem-dashboard-tool.git
cd siem-dashboard-tool
```

2. Install dependencies:
```bash
pip install flask
```

3. Run the application:
```bash
python siem_dashboard.py

or run the alternative version:
python siem_dashboard_second_version.py
```

4. Open your browser and navigate to `http://127.0.0.1:5000`

## Example Usage
Add a new simulated log entry via API:
```bash
curl -X POST http://127.0.0.1:5000/api/add_log \
-H "Content-Type: application/json" \
-d '{"source": "WAF", "event": "Cross-Site Scripting detected", "severity": "High"}'
```

## Real-World Detection Write-Up
This tool simulates events such as:
- Port scanning (Nmap probes)
- SQL Injection attacks (captured by IDS)
- Brute-force login attempts (detected by auth logs)

These types of events are commonly monitored in enterprise SIEMs to correlate threat activity and trigger incident response.

## Future Enhancements
- Integrate with real logs from syslog, AWS CloudWatch, or Elastic Beats
- Add alerting functionality
- Role-based user access
- Add visual graphs using Chart.js or D3.js

## License
MIT License

## Disclaimer
This tool is provided as-is for educational and research purposes. Do not use it in a production environment without proper configuration and security reviews.
