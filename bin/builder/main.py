#main notebook generator

from dir_scanner_3 import *
#from doc_parser import *
from jinja import *
from dropbox import DropboxLink
from server import StartServer
from make_index import MakeIndex
import socket

notebook_dir = '/Users/christophermackay/Desktop/Coding/lab-notebook/notebook'

folders = treeScanner(notebook_dir)


for folder in folders:
	subfolders = []
	for other_folder in folders:
		if other_folder.parent == folder.name:
			subfolders.append(other_folder)
	MakeIndex(folder, subfolders)

#make a site map...(

#set the ip address and port in the dropbox file

ip = socket.gethostbyname(socket.gethostname())

server_dir = ip+':8000/notebook/'

DropboxLink(server_dir)

#start server

to_serve = '/Users/christophermackay/Desktop/Coding/lab-notebook/'
StartServer(to_serve)