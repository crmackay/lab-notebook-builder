def MakeIndex(folder, subfolders):
	
	from jinja2 import FileSystemLoader, Environment
	
	from html_editing import HTMLEditor
	
	my_loader = FileSystemLoader('/Users/christophermackay/Desktop/Coding/lab-notebook/notebook_builder/templates/')

	env = Environment(loader=my_loader)
	
	root = folder.root.split('/')
	
	static_root = ''
	
	level = len(root)-root.index('lab-notebook')
	
	for i in range(level):
		static_root += ('../')
	
	static_root += 'notebook_builder/static/'
	
	if folder.type == 'experiment':
		template = env.get_template('experiment.html')
		page = template.render(exp=folder, subfldrs = subfolders, static_root=static_root)
	else:
		template = env.get_template('folder.html')
		page = template.render(fldr=folder, subfldrs = subfolders, static_root=static_root)

	
	page = page.split('\n')
	
	for i, line in enumerate(page):
		new_line = HTMLEditor(line)
		page[i] = new_line
	
	page = '\n'.join(page)
	
	with open(folder.root+'/'+folder.name+'/index.html', 'w') as output:
		output.write(page)
	