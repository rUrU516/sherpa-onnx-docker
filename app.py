import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", "9000"))


class Handler(BaseHTTPRequestHandler):
    def _write(
        self, code: int, body: str, content_type: str = "text/plain; charset=utf-8"
    ):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        if self.path in ["/", "/health", "/ready"]:
            self._write(200, "ok")
            return

        if self.path == "/cuda":
            cuda_home = os.environ.get("CUDA_HOME", "")
            self._write(200, f"cuda container alive\nCUDA_HOME={cuda_home}\n")
            return

        self._write(404, "not found")

    def do_POST(self):
        if self.path == "/invoke":
            content_length = int(self.headers.get("Content-Length", "0"))
            body = (
                self.rfile.read(content_length).decode("utf-8")
                if content_length > 0
                else ""
            )
            self._write(200, f"received: {body}")
            return

        self._write(404, "not found")

    def log_message(self, format: str, *args):
        print("[http]", format % args)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"server listening on 0.0.0.0:{PORT}")
    server.serve_forever()
