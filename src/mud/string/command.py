
class Command():
	
	commands = [
		["go", "Go somewhere. Followed by destination key."], 
		["attack", "Attack something. Followed by the target to attack."], 
		["examine", "Examine something. Followed by the target to examine"], 
		["help", "Displays this help message"],
		["quit", "Exit the game. Your state will be saved"]]
	
	def commandlist(self):
		l = []
		for i,item in enumerate(self.commands):
			l.append(item[0])
		return l
	
	def help(self, command):
		if self.commands[command]:
			return self.commands[command]
		return "Unkown command"
