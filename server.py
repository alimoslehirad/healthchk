import http.server
import socketserver
import threading

class ServerSide(threading.Thread):


    def run(self):
        self.PORT = 5035
        self.Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", self.PORT), self.Handler) as httpd:
            print("serving at port", self.PORT)
            httpd.serve_forever()