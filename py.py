#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
from datetime import date
import calendar
my_date = date.today()
day = calendar.day_name[my_date.weekday()]




array = []

#for i in dayjson.values():
 #   array.append(i)


newest = "".join(array)

mydata = '''
{
"speech": '''+newest+''',
"displayText": '''+newest+''',
"data": {},
"contextOut": [],
"source": "DuckDuckGo"
}'''

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        #prints posted data
        print("\n----- Request Start ----->\n")

        request_headers = self.headers
        content_length = request_headers.getheaders('content-length')
        length = int(content_length[0]) if content_length else 0
        
        
        jsonload = self.rfile.read(length)
        strjsonload = str(jsonload)
        print("\n<----- Request End -----\n")

        with open('lessons.json') as data_file:  
            data = json.load(data_file)


        datagot = json.load(jsonload)
        timenow = datagot["result"]["parameters"]["number"].values()
        dayjson = data[day][timenow]

        print dayjson



        #POST response

        self._set_headers()
        self.wfile.write(mydata)
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
