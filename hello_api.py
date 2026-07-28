"""
A simple REST API for the "Hello, World!" service.

No external dependencies required — uses only the Python standard library.

Endpoints:
    GET /api/hello          -> {"message": "Hello, World!"}
    GET /api/hello?name=Bob -> {"message": "Hello, Bob!"}

Run:
    python3 hello_api.py
Then open http://localhost:8000/api/hello
"""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HOST = "0.0.0.0"
PORT = 8000


def build_message(name: str | None) -> str:
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


class HelloHandler(BaseHTTPRequestHandler):
    def _send_json(self, payload: dict, status: int = 200) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/hello":
            name = parse_qs(parsed.query).get("name", [None])[0]
            self._send_json({"message": build_message(name)})
        elif parsed.path == "/":
            self._send_json({"message": build_message(None)})
        else:
            self._send_json({"error": "Not found"}, status=404)

    # Keep the console quiet for routine requests.
    def log_message(self, format: str, *args) -> None:  # noqa: A002
        return


def main() -> None:
    server = ThreadingHTTPServer((HOST, PORT), HelloHandler)
    print(f"Hello API running at http://{HOST}:{PORT}/api/hello")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.shutdown()


if __name__ == "__main__":
    main()
