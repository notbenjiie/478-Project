import re
import json
import os
from collections import Counter

def process_logs():
    # File paths based on your repo structure
    log_path = 'logs/access.log'
    metrics_json_path = 'artifacts/release/metrics.json'
    
    # Ensure the artifacts directory exists
    os.makedirs('artifacts/release', exist_ok=True)

    ips = []
    total_attempts = 0

    # Regex to find IP addresses at the start of a line (Standard Flask/Nginx format)
    ip_pattern = re.compile(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    if not os.path.exists(log_path):
        print(f"Error: {log_path} not found. Please run 'make demo' first to generate traffic.")
        return

    with open(log_path, 'r') as f:
        for line in f:
            total_attempts += 1
            match = ip_pattern.match(line)
            if match:
                ips.append(match.group(1))

    # Calculate Security Metrics
    unique_ips = list(set(ips))
    top_attacker = Counter(ips).most_common(1)[0] if ips else ("None", 0)
    
    # Structure the data for Section C "Observability"
    metrics = {
        "release_metadata": {
            "version": "Alpha-Beta-Integrated",
            "component": "Harbor-Portal-Honeypot"
        },
        "traffic_summary": {
            "total_request_count": total_attempts,
            "unique_attacker_count": len(unique_ips),
            "flagged_ips": unique_ips
        },
        "threat_intelligence": {
            "primary_source_ip": top_attacker[0],
            "incident_count": top_attacker[1],
            "risk_level": "High" if total_attempts > 10 else "Low"
        }
    }

    # Export to JSON (Requirement: Observability Artifact)
    with open(metrics_json_path, 'w') as jf:
        json.dump(metrics, jf, indent=4)

    print(f"Success: Security metrics exported to {metrics_json_path}")

if __name__ == "__main__":
    process_logs()
