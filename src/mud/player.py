from enum import Enum
from mud.string.message import Message as M
from mud.string.command import Command

class PlayerState(Enum):
	
	UNKNOWN = 1
	NEW = 2

class Player():
	
	messagequeue = []
	state = PlayerState.UNKNOWN
	c = Command()
	
	def add(self, m):
		self.messagequeue.append(m)
		
	def clear(self):
		self.messagequeue = []
	
	# actually handle player action
	def do(self, action, trail):
		if action == "help":
			for i in self.c.commandlist():
				if trail.startswith(i):
					self.add(i + " - " + self.c.help(i) + "\n")
					return
			self.add(M.help())
			string = ""
			for i in self.c.commandlist():
				string = string + " " + i
			self.add(string + "\n")
		else:
			self.add(M.no_effect())

