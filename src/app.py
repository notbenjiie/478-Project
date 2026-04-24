from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import os

# Ensure log directory exists
os.makedirs("/var/log/app", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="/var/log/app/access.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]

        # Simple analysis step
        if "admin" in self.path.lower():
            label = "SUSPICIOUS"
        else:
            label = "NORMAL"

        log_entry = f"{label} GET {self.path} from {ip}"
        logging.info(log_entry)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(f"{label}: Hello from honeypot\n".encode())

# Start server
server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Honeypot running on port 8080...")
server.serve_forever()