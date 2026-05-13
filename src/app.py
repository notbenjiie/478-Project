from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

SENSITIVE_PATHS = {
    "/admin",
    "/login",
    "/wp-admin",
    "/phpmyadmin",
    "/ssh",
}

request_counts = {}


def classify_request(path, source_ip):
    score = 0
    reasons = []

    path = path.lower()
    current_hour = datetime.now().hour

    if path in SENSITIVE_PATHS:
        score += 2
        reasons.append("sensitive_endpoint")

    request_counts[source_ip] = request_counts.get(source_ip, 0) + 1

    if request_counts[source_ip] >= 5:
        score += 1
        reasons.append("repeated_requests")

    if current_hour < 6 or current_hour > 22:
        score += 1
        reasons.append("off_hours_access")

    if score >= 2:
        return "SUSPICIOUS", score, reasons

    return "NORMAL", score, reasons


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def honeypot(path):
    full_path = "/" + path
    source_ip = request.remote_addr

    classification, score, reasons = classify_request(full_path, source_ip)

    log_line = (
        f"{datetime.now()} {classification} GET {full_path} "
        f"from {source_ip} score={score} reasons={','.join(reasons) or 'none'}\n"
    )

    with open("/var/log/app/access.log", "a") as log_file:
        log_file.write(log_line)

    return f"{classification}: Hello from honeypot\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
