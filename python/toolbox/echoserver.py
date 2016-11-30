#!/usr/bin/env python3
import argparse
import http
import http.server


class HelloHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(http.HTTPStatus.OK)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello.\n")


class EchoHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        raise NotImplementedError("Not working")
        request_body = self.rfile.read(int(self.headers['Content-Length']))
        self.send_response(http.HTTPStatus.OK)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(request_body)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', help='hostname', default='127.0.0.1')
    parser.add_argument('-p', '--port', help='port', type=int, default=4444)
    args = parser.parse_args()

    handler_class = EchoHandler
    server = http.server.HTTPServer((args.host, args.port), handler_class)
    try:
        print("Serving %s on %s:%d" %
              (handler_class, args.host, args.port))
        server.serve_forever()
    except KeyboardInterrupt:
        print("Exiting.")
