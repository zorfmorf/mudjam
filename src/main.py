import socket
import threading
import socketserver
import mud.server as serv

finish = False


if __name__ == "__main__":
	HOST, PORT = "localhost", 4183
	
	# Create server object
	server = serv.ThreadedTCPServer((HOST, PORT), serv.ThreadedTCPRequestHandler)
	ip, port = server.server_address
	
	# 
	server_thread = threading.Thread(target=server.serve_forever)
	# Exit the server thread when the main thread terminates
	server_thread.daemon = True
	
	print("Starting server")
	server_thread.start()
	
	while not finish:
		pass
	
	server.shutdown()
	print("Server finished")
