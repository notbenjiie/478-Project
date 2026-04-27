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
`Linux (ubuntu)`

or 

`Windows`

## Run the full demo
`demo.bat` for windows
`make up && make down` for linux
This will:
- Start Docker containers
- Send test requests
- Generate logs and metrics

## Manual Steps for Windows 

start the system:

`docker-compose up -d --build`

3. simulate traffic
- `curl http://localhost:8080 (normal)`
- `curl http://localhost:8080/admin (suspicious)`
- `curl http://localhost:8080/test (normal)`

4. View logs
   
`type logs\access.log`

- log records all incoming requests and classifications
  
5. Generate metrics
   
`python src\generate_metrics.py`

7. View results
   
`type artifacts\release\metrics.json`
- this file contains a summary of total requests, normal traffic, and suspicious activity

## Demo Video Windows
[watch Demo](DOCS/demo.mp4)

## Demo Video Linux


## Security Invariants
1. **Zero Trust Logging:** The system assumes all traffic to the decoy is malicious.
2. **Data Isolation:** Captured credentials are never stored in the production DB; they remain in isolated forensic logs.
3. **Least Privilege:** All containers run with restricted CPU/Memory.

Example behavior 
request  
- /
- /admin
- /test

classification

- NORMAL
- SUSPICIOUS
- NORMAL

Example log entries
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
  
Example output:
- NORMAL → /
- SUSPICIOUS → /admin
- NORMAL → /test

Metrics are exported to:

- NORMAL → /
- SUSPICIOUS → /admin
- NORMAL → /test

Metrics are exported to:

`artifacts/release/metrics.json`
