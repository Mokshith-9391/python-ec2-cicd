from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8000


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = "Hello Mokshith "

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

    def log_message(self, format, *args):
        print(f"[HTTP] {self.address_string()} - {format % args}")


def run_server():
    server = HTTPServer((HOST, PORT), RequestHandler)

    print(f"Server running on {HOST}:{PORT}")

    server.serve_forever()


if __name__ == "__main__":
    run_server()