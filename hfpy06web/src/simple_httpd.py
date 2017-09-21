
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8085

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

# http://127.0.0.1:8085/