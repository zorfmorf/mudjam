
class Command():
	
	commands = ( 
		("go", "Go somewhere. Followed by destination key."), 
		("attack", "Attack something. Followed by the target to attack."), 
		("examine", "Examine something. Followed by the target to examine"), 
		("help", "Displays this help message"),
		("quit", "Exit the game. Your state will be saved"))
	
	def commandlist(self):
		
		return ( "go", "attack", "examine", "help", "quit")
	
	def help(self, command):
		if self.commands[command]:
			return self.commands[command]
		return "Unkown command"
