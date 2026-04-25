import json
import csv
from collections import Counter

def process_logs():
    incidents = []
    #log path
    log_path = 'logs/access.log'
    
    with open(log_path, 'r') as f:
        for line in f:
            # log is JSON-formatted per line
            incidents.append(json.loads(line))

    # Calculate Metrics
    total_attempts = len(incidents)
    ips = [i['src_ip'] for i in incidents]
    top_attacker = Counter(ips).most_common(1)[0] if ips else ("None", 0)
    
    metrics = {
        "summary": {
            "total_probes": total_attempts,
            "unique_attackers": len(set(ips)),
            "top_threat_actor": top_attacker[0],
            "threat_intensity": top_attacker[1]
        }
    }

    # Export to JSON
    with open('artifacts/release/metrics.json', 'w') as jf:
        json.dump(metrics, jf, indent=4)
        
    # Export to CSV for the "Charts" requirement
    with open('artifacts/release/attack_summary.csv', 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Probes", total_attempts])
        writer.writerow(["Top IP", top_attacker[0]])

if __name__ == "__main__":
    process_logs()
