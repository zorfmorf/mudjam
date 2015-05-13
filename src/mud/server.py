import socket
import threading
import socketserver
import time
from mud.string.message import Message as M
from mud.player import Player
from mud.string.command import Command as C

# if message m contains any of the elements in list l
def contains(m, l):
	for c in l:
		if c in m:
			return True
	return False

def commandlist()
	commands = []
	for name, member in C.__members__.items():
		commands.append(name)
	return commands

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	player = None
	
	def setup(self):
		self.player = Player()
	
	def send(self, message):
		self.request.sendall(bytes( message, 'ascii'))
	
	def recv(self, mlist):
		data = " " + str(self.request.recv(2), 'ascii')
		data = data.lower()
		
		# read data until one of given options is found
		while not contains(data, mlist):
			data += str(self.request.recv(1), 'ascii')
			data = data.lower()
			
		# return recieved given option
		for i in mlist:
			if i in data:
				return i
	
	def handle(self):
		self.send(M.welcome())
		
		# Load or create character
		while self.player.state == PlayerState.UNKOWN:
			self.send(M.new_player())
			answer = self.recv(("yes", "no"))
			if answer == "yes":
				self.send(M.create())
			else:
				self.send(M.load())
		
		# Recieve commands and
		answer = self.recv(commandlist())
		while not (answer == C.)
		
		global finish
		finish = True
	
	def finish(self):
		pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass
