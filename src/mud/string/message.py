from mud.string.colors import AnsiColors as C

class Message:

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
		return ""
	
	def load():
		return "Enter the key for the saved character\n"
 
