import socket
import threading
import socketserver
import time
from mud.string.message import Message as M
from mud.player import Player
from mud.player import PlayerState
from mud.string.command import Command as C

# if message m contains any of the elements in list l
def contains(m, l):
	for c in l:
		if c in m:
			return True
	return False

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	player = None
	c = None
	
	def setup(self):
		self.player = Player()
		self.c = C()
	
	def send(self, message):
		self.request.sendall(bytes( message, 'ascii'))
		
	def sendall(self):
		for i in self.player.messagequeue:
			self.send(i)
		self.player.clear()
	
	def recv(self, mlist):
		data = " " + str(self.request.recv(1024), 'ascii')
		data = data.lower()
		
		# read data until one of given options is found
		while not contains(data, mlist):
			if contains(data, ["\\n"]):
				self.send(M.hint())
			data += str(self.request.recv(1024), 'ascii')
			data = data.lower()
			
		# return recieved given option
		for i in mlist:
			if i in data:
				data = ""
				return i
	
	def handle(self):
		self.send(M.welcome())
		
		# Load or create character
		while self.player.state == PlayerState.UNKNOWN:
			self.send(M.new_player())
			answer = self.recv(["yes", "no"])
			if answer == "yes":
				self.send(M.create())
				self.player.state = PlayerState.NEW
			else:
				self.send(M.load())
		
		# Recieve commands and handle them
		self.send(M.hint())
		answer = self.recv(self.c.commandlist())
		while not (answer == "quit"):
			self.player.do(answer)
			self.sendall()
			time.sleep(0.5)
			answer = self.recv(self.c.commandlist())
		
	
	def finish(self):
		pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass
