from enum import Enum
from mud.string.message import Message as M

class PlayerState(Enum):
	
	UNKNOWN = 1
	NEW = 2

class Player():
	
	messagequeue = []
	state = PlayerState.UNKNOWN
	
	def add(self, m):
		self.messagequeue.append(m)
		
	def clear(self):
		self.messagequeue = []
	
	# actually handle player action
	def do(self, action):
		if action == "help":
			self.add(M.help())
		else:
			self.add(M.no_effect())

