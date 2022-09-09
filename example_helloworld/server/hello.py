# Example slightly modified from
# https://docs.python.org/3/library/http.server.html

import http.server
import socketserver
from pathlib import Path

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server, directory=None):
        if directory is None:
            directory = Path(__file__).parent
        super().__init__(request, client_address, server, directory=directory)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()