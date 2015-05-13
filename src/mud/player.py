from enum import Enum

class PlayerState(Enum):
	
	UNKNOWN = 1
	NEW = 2

class Player():
	
	def __init__(self):
		self.state = PlayerState.UNKNOWN

