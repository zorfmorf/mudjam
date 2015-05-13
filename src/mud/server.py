import socket
import threading
import socketserver
import timer
from mud.string.colors import AnsiColors as C

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	def send(self, message):
		self.request.sendall(bytes( message, 'ascii'))
	
	def setup(self):
		pass
	
	def handle(self):
		global C
		self.send("".join(("Welcome to ", C.GREEN, "TestMUD", C.SANE, "\n!")))
		#data = str(self.request.recv(1024), 'ascii')
		#cur_thread = threading.current_thread()
		#response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
		#self.request.sendall(response)
		global finish
		finish = True
	
	def finish(self):
		pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass
