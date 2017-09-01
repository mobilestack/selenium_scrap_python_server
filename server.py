

#!/home/tony/.envs/p35/bin/python

"""
This is modified from a github fork from
https://gist.github.com/mobilestack/f3370618a098c8b57e58055eb14aec60

This works for python3

Very simple HTTP server in python.
Usage::
    ./server.py [<port>]
    note that you need sudo to run on 80 port
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "url=http://foo.bar" http://localhost
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from selenium_render import selenium_render as sr
import json


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b"<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        data = json.loads(post_body.decode('utf8'))
        print('data is {}'.format(data))
        url = data['url']
        print('url {}'.format(url))        
        html = sr(url)
        
        self.wfile.write(html.encode())        

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()


