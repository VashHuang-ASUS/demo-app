from http.server import HTTPServer, BaseHTTPRequestHandler
import os


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        version = os.getenv("APP_VERSION", "v1.0.1")
        body = f"version: {version}\n".encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass  # suppress default access log


HTTPServer(("", 8080), Handler).serve_forever()
