def StartServer(notebook_dir):

	import SimpleHTTPServer
	import SocketServer
	import os

	os.chdir(notebook_dir)

	PORT = 8000

	Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

	httpd = SocketServer.TCPServer(('',PORT),Handler)

	print 'serving at port: ', PORT

	httpd.serve_forever()