import socket
import threading
import socketserver
import time
from mud.string.message import Message as M
from mud.player import Player

# if message m contains any of the elements in list l
def contains(m, l):
	for c in l:
		if c in m:
			return True
	return False

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	player = None
	
	def setup(self):
		self.player = Player()
	
	def send(self, message):
		self.request.sendall(bytes( message, 'ascii'))
	
	def recv(self, mlist):
		data = " " + str(self.request.recv(2), 'ascii')
		data = data.lower()
		while not contains(data, mlist):
			data += str(self.request.recv(1), 'ascii')
			data = data.lower()
		return data
	
	def handle(self):
		self.send(M.welcome())
		self.send(M.new_player())
		data = self.recv(("yes", "no"))
		if "yes" in data:
			self.send("Lets get you registered\n")
			
		if "no" in data:
			self.send("Welcome bag, Mr. Fancypants\n")
		
		#response = bytes("Eyyyyy", 'ascii')
		#self.request.sendall(response)
		#self.send("".join(("Welcome to ", C.GREEN, "TestMUD", C.SANE, "\n!")))
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
