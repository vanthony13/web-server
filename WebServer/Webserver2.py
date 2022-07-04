import sys, os, socket
from socketserver import ThreadingMixIn
from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = socket.gethostname()

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

'''
This sets the listening port, default port 80
'''
if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 3000

'''
This sets the working directory of the HTTPServer, defaults to directory where script is executed.
'''
if sys.argv[2:]:
    os.chdir(sys.argv[2])
    CWD = sys.argv[2]
else:
    CWD = os.getcwd()

server = ThreadingSimpleServer(('192.168.43.241', PORT), SimpleHTTPRequestHandler)
print("Serving HTTP traffic from", CWD, "on", HOST, "using port", PORT)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("\nShutting down server per users request.")


