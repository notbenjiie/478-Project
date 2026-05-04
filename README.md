# 478-Project
Overview
Your final project is a semester-long, reproducible build of a security-focused system. You may work solo or in pairs (pairs must deliver roughly 50% more scope). The goal of the proposal is to define a clear, achievable, and technically sound plan for the remainder of the term.

Your project should demonstrate:
- A meaningful security problem or system enhancement.
- A reproducible build and evaluation process.
- Ethical awareness and responsible handling of security-related data.
- Clear alignment with course labs and learning outcomes.

Project Overview: Our goal is to mitigate cyber attacks by creating honeypot instances where attackers are fed bait and if they take it, we begin capturing their packets and measuring consequences as well as circumstances. We plan on creating fake admin or other private documents/sites to enact as attention holders while we continue capturing their data. It'll then be sent to our observer who will store that pcap file and analyze for suspicious packets.

Setup Overview: We must setup this github repo, docker instances of the decoy and the observer, creating the honey tokens and fake sites, as well as the pcapture on the observer(making sure it saves the file properly). Once that is all done we can polish and 'create' the fake files or bait, whichever direction we head in to ensure the bait is believable and keeps the attacker clicking. 

## How to run

requirements
- docker
- docker compose
- Make

## Quick Start (Reccommended)
Run the full system

`make up && make demo`

This command will:
- Start the honeypot system
- Send test requests
- Classify traffic (NORMAL / SUSPICIOUS)
- Display logs
- Generate security metrics

Example output:
- NORMAL: Hello from honeypot
- SUSPICIOUS: Hello from honeypot
- NORMAL: Hello from honeypot

Logs:
- NORMAL GET /
- SUSPICIOUS GET /admin

## Demo Video #1
[watch Demo](DOCS/demo.mp4)

## FINAL DEMO VIDEO LINK
[View Slides](https://docs.google.com/presentation/d/10t-NMCDJtPISPto_gt5wPFp6Cvo3L-zI0VWYqFeTZIw)

## FINAL PROJECT REPORT PDF
[CECS 478 Final Report.pdf](https://github.com/user-attachments/files/27327317/CECS.478.Final.Report.pdf)

## Security Invariants
1. **Zero Trust Logging:** The system assumes all traffic to the decoy is malicious.
2. **Data Isolation:** Captured credentials are never stored in the production DB; they remain in isolated forensic logs.
3. **Least Privilege:** All containers run with restricted CPU/Memory.

Example request:

- `/` → NORMAL  
- `/admin` → SUSPICIOUS  
- `/test` → NORMAL  

Example log entries:
- NORMAL GET /
- SUSPICIOUS GET /admin

## Artifacts
- all generated evidence is stored in:
`artifacts/release/`

includes: 
- metrics.json (Summary of system activity)
- evidence.pcap (Captured network traffic)

## Runbook
### Full Rebuild and Run
1. `make clean` (Remove old artifacts)
2. `make up` (Build and start containers)
3. `make demo` (Run the automated attack simulation)

### Evidence Generation
1. Run `python3 src/generate_metrics.py` to refresh JSON/CSV metrics.
2. Check `artifacts/release/` for the latest logs.

## Evaluation Summary
the system successfully:
- Classifies requests as normal or suspicious
- Logs all activity
- Generates structured metrics for analysis

  ## Reproducibility

Run the following command on a fresh clone:

`make clean && make up && make demo`

example classification:
- NORMAL → `/`
- SUSPICIOUS → `/admin`
- NORMAL → `/test`

## Metrics output
metrics are exported to:

`artifacts/release/metrics.json`
