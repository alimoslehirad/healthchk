import http.server
import socketserver
class ServerSide:


    def __init__(self):
        self.PORT = 5035
        self.Handler = http.server.SimpleHTTPRequestHandler

    def socketing(self):

        with socketserver.TCPServer(("", self.PORT), self.Handler) as httpd:
            print("serving at port", self.PORT)
            httpd.serve_forever()