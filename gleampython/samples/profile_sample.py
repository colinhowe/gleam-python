from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import time

import gleam_compiler

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith(".js"):
            path = curdir + sep + self.path
            path = os.path.normpath(path)
            if not path.startswith(curdir):
                self.send_error(404,'File Not Found: %s' % self.path)
                return

            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        # Compile the gleam file
        #
        gleam_compiler.compile_gleam('samples/profile.gleam', 'samples/gleam_profile.js', 'samples/gleam_profile.py')

        # Run it
        #
        f = file('samples/gleam_profile.py')
        src = f.read()
        f.close()
        code = compile(src, 'gleam_profile.py', 'exec')
        ns = {}
        exec(code) in ns
        print ns
        

        # Serve the HTML
        #
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        return

def main():
    try:
        server = HTTPServer(('', 8000), MyHandler)
        print 'Started httpserver on port 8000...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
