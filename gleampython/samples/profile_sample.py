from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import os
import time

import gleam_compiler
import to_html

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith(".js"):
            path = curdir + sep + self.path
            path = os.path.abspath(path)
            cwd = os.path.abspath(curdir) 
            print path
            print cwd
            if not path.startswith(cwd):
                self.send_error(404,'File Not Found: %s' % self.path)
                return

            f = open(cwd + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        # Compile the gleam file
        #
        gleam_compiler.compile_gleam('samples/profile.gleam', 'samples/gleam_profile.js', 'samples/gleam_profile.py')

        # Run it
        #
        import python_runner
        gleam = python_runner.Runner()
        execfile('samples/gleam_profile.py', {'gleam': gleam}, {})

        # Serve the HTML
        #
        print gleam
        result = to_html.HtmlCreator().as_html(gleam.nodes)
        result = '%s' % result
        result = """<script type="text/javascript" src="gleam.js" ></script>
<script type="text/javascript" src="samples/gleam_profile.js" ></script>
""" + result

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(result)
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
