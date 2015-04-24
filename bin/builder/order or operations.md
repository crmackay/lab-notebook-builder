# order of operations

1. fix links to sub folders (sidebar? dropdown menu?)

1. work on todo list
	1. day views...
	1. @due:2014-10-10, @ desk 

1. work on dropbox

1. work on header/sidebar

1. work on detecting changes to the directory and re-processing (esp when server is running)

1. create a script that can be double-clicked to run server/app

1. add js alert..checking boxes are not saved

1. add support for data files

1. add support for other '.md' files

1. simple app to store checked tasks

	- use simple wsgi server [here](https://docs.python.org/2/library/wsgiref.html#module-wsgiref.simple_server)
	- and or flask app to handle AJAX requests to change the underlying files..
	- login mechanism
	- cookie mechanism
	- store changes


# new idea

- webdav server of filesystem of notebook:
	- any changes are re-rendered
- web server 
	- first a static site
	- serves the same filesystem with editing, adding capailities 