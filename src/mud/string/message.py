from mud.string.colors import AnsiColors as C

class Message:
	
	def goodbye():
		return "Thanks for playing!\n"
	
	def hint():
		return "Type \"help\" if you are unsure what to do.\n"
	
	def no_effect():
		return "This doesn't do anything.\n"
	
	def help():
		return "This is a list of all possible commands:\n"

	def welcome():
		return "".join(( "\n         Welcome to\n\n", C.GREEN,
		"                  _       _                 _ \n",
		"  /\/\  _   _  __| |     (_) ___/\   /\__ _| |\n",
		" /    \| | | |/ _` |_____| |/ _ \ \ / / _` | |\n",
		"/ /\/\ \ |_| | (_| |_____| |  __/\ V / (_| | |\n",
		"\/    \/\__,_|\__,_|     |_|\___| \_/ \__,_|_|\n",
		"                                              \n",
		"\n", C.SANE, " Created during the ", C.BLUE,"MUDJAM 2105", C.SANE,
		" by ", C.GREEN, "Sebastian Tauch", C.SANE, "\n"))

	def new_player():
		return "Do you want to create a new character? (Yes/No)\n"
	
	def create():
		return "Creating new player.\n"
	
	def load():
		return "Enter the key for the saved character\n"
 
