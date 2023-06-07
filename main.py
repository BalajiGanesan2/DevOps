import http.server
import socketserver

# Define the port number to run the server on
PORT = 8000

# Define the request handler class
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass

# Create an instance of the server
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
