import socket
import threading
import socketserver
import time
from mud.string.message import Message as M
from mud.player import Player
from mud.player import PlayerState
from mud.string.command import Command as C


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	player = None
	c = None
	
	def setup(self):
		self.player = Player()
		self.c = C()
	
	def send(self, message):
		self.request.sendall(bytes( message, 'ascii'))
	
	# send all queued messages for this player
	def sendall(self):
		for i in self.player.messagequeue:
			self.send(i)
		self.player.clear()
	
	# Recieve data and check if the answer starts
	# with any of the items in the given list
	def recv(self, mlist):
		data = None
		while data == None:
			data = str(self.request.recv(1024), 'ascii')
		
		data = data.lower()	
		
		for i in mlist:
			if data.startswith(i):
				return i, data[len(i):]
		
		# Return a string bc we HAVE recieved data
		# that was invalid (-> answer required)
		return "None"
	
	# Retry recieving until some answer is recieved
	def recv_until(self, mlist):
		answer = None
		trail = None
		while answer == None:
			answer, trail = self.recv(mlist)
		return answer, trail
	
	def handle(self):
		self.send(M.welcome())
		
		# Load or create character
		while self.player.state == PlayerState.UNKNOWN:
			self.send(M.new_player())
			answer, trail = self.recv(["yes", "no"])
			if answer == "yes":
				self.send(M.create())
				self.player.state = PlayerState.NEW
			if answer == "no":
				self.send(M.load())
		
		# Recieve commands and handle them
		self.send(M.hint())
		answer, trail = self.recv_until(self.c.commandlist())
		while not (answer == "quit"):
			print( "recieved", answer, trail)
			self.player.do(answer, trail)
			self.sendall()
			time.sleep(0.2)
			answer = self.recv(self.c.commandlist())
		self.send(M.goodbye())
		
	
	def finish(self):
		pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass
