#!/usr/bin/python
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer
import draw


class CORSRequestHandler (SimpleHTTPRequestHandler):
	def end_headers (self):
		self.send_header('Access-Control-Allow-Origin', '*')
		SimpleHTTPRequestHandler.end_headers(self)
	def do_POST(s):
		"""Respond to a GET request."""
		if s.path == '/execute':
			json = draw.begin_draw()
		
		s.send_response(200)
		s.send_header("Content-type", "text/json")
		s.end_headers()
		s.wfile.write(json)

if __name__ == '__main__':
		BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)