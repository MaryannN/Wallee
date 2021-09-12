#from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import json
import wikipedia ## download with 'pip install wikipedia' 

#class handler(BaseHTTPRequestHandler):
#    def do_GET(self):
#        self.send_response(200)
#        self.send_header('Content-type','text/html')
#        self.end_headers()

#        message = searchword
#        self.wfile.write(bytes(message, "utf8"))

#with HTTPServer(('', 8000), handler) as server: ##connected to port 8000
#    server.serve_forever()

form = cgi.FieldStorage()
searchterm = "apple" #form.getvalue('insert')
print(searchterm)

definition = wikipedia.summary(searchterm, sentences = 3, auto_suggest=False)
print(definition)