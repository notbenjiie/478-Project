Initial Evaluation Results
Current Observations:
  Detection Latency: The honeypot successfully triggers the forensic-sniffer within <150ms of a failed login attempt.
  Data Quality: Captured PCAPs clearly show the POST body, including the plaintext credentials used by the attacker.
  Effectiveness: 100% of unauthorized attempts were correctly classified as "PROBE" and logged to access.log.
