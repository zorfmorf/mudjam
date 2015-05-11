import socket
import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
	
	def setup(self):
		pass
	
	def handle(self):
		self.request.sendall(bytes("Welcome to \u001B[0;34mTestMUD\u001B[0m \n\nYou are eaten by a Bos Mutus.\n\n You are \u001B[0;31mdead\u001B[0m.\n\n", 'ascii'))
		#data = str(self.request.recv(1024), 'ascii')
		#cur_thread = threading.current_thread()
		#response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
		#self.request.sendall(response)
		global finish
		finish = true
	
	def finish(self):
		pass

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	pass
