#doc processing and parsing


#create an entry class

projects = set()

import markdown
import os
import time

class entry(object):
	'''creates an entry class'''
	
	def __init__(self,experiment, project, type, content, year, month, day, root)
		
		self.experiment = experiment
		self.project = project
		self.type = type
		self.content = content
		self.year = year
		self.month = month
		self.day = day
		self.root = root
			
class experiment(object):
	def __init__(self, name, project, intro, entries, conclusion, data, todos, status):
		self.name = name
		self.project = project
		self.intro = intro
		self.entries = entries
		self.conclusion = conclusion
		self.data = data
		self.todos = todos
		self.status = status

class project(object):
	def __init__(self, name, experiments):
		self.name = name
		self.experiments = experiments

file_stats = os.stat(path)

last_modified=localtime(file_stats.st_mtime)
year = last_modified.tm_year
month = last_modified.tm_mon
day = last_modified.tm_mday

experiments = []
projects = []
entries = []

def make_objects(folders):
	for folder in folders:
		if folder.name == 'projects':
			for subfolder in folder.subfolders:
				object = project(name=subfolder)
				projects.append(object)
		elif folder == 