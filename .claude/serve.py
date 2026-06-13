import http.server, os
os.chdir('/Users/cyl/Desktop/yileic.github.io')
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8787, bind='127.0.0.1')
