from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os

LOG_DIR = os.environ.get("HONEYPOT_LOG_DIR", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "access.log"),
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

def classify_path(path):
    """
    Classify incoming request paths.
    Any path containing 'admin' is considered suspicious.
    """
    if "admin" in path.lower():
        return "SUSPICIOUS"
    return "NORMAL"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]

        label = classify_path(self.path)

        log_entry = f"{label} GET {self.path} from {ip}"
        logging.info(log_entry)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"{label}: Hello from honeypot\n".encode())

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), Handler)
    print("Honeypot running on port 8080...")
    server.serve_forever()