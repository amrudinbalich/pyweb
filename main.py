# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# error reporting

from http.server import HTTPServer, BaseHTTPRequestHandler
from helpers import view
import logging
import json

logging.basicConfig(level=logging.DEBUG)

class CustomHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type:', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(view('index'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        # Process post_data here...
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "POST received"}).encode("utf-8"))


if __name__ == '__main__':
    s =  HTTPServer(('127.0.0.1', 8080), CustomHTTPHandler)
    s.serve_forever()