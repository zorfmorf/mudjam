import socket
import threading
import socketserver
from mud.string.colors import AnsiColors as C

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	def setup(self):
		pass
	
	def handle(self):
		global C
		self.request.sendall(bytes( "".join(("Welcome to ", C.GREEN, "TestMUD", C.SANE, "\n\nYou are eaten by a Bos Mutus.\n\n You are \u001B[0;31mdead\u001B[0m.\n\n")), 'ascii'))
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
