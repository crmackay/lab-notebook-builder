#attempt #3

def treeScanner(directory):
    import os
    import re
    from datetime import date
    from markdown_processor import processMD
    
    class Folder(object):
        """This is the folder Class
        
        attributes:
            self.name - the name in the filesystem for the folder
            self.root - the root filesystem path to the folder
            self.files - a list of files within the folder
            self.entries - a list of markdown
            self.type - the type of folder 
                        default is 'folder'
            self.parent - the containing folder
        """
        
        def __init__(self, name, root):
            self.name = name
            self.root = root
            self.files = []
            self.entries = []
            self.type = 'folder'
            self.parent = root.split('/')[-1]
        
        def makeExperiment(self):
            print self.name
            self.status = 'active'
            self.data = []
            #print self.entries
            file_list = self.files
            for file in file_list:
                #print file.name
                if file.type == 'entry':
                    if file.entry_type == 'dated-entry':
                        self.entries.append(file)
                    elif file.entry_type == 'intro':
                        self.intro = file
                    elif file.entry_type == 'conclusions':
                        self.conclusions = file
                        self.status = 'completed'
                    elif file.entry_type == 'todos':
                        self.todos = file
                else:
                    self.data.append(file)

            if self.entries is not None:
                self.entries.sort(key = lambda x: x.date)

            
            self.start = self.entries[0].date
            if self.status == 'completed':
                self.end = self.entries[-1].date
            else:
                self.status = 'active'
            self.type = 'experiment'
            
        def makeProject(self):
            self.experiments = []
            self.type = 'project'
            
        
    class File(object):
        def __init__(self, name, root):
            self.name = name
            self.root = root
            self.uri = root+'/'+name
            self.parent = root.split('/')[-1]
            self.entry_type = None
            if '.md' in name:
                self.type = 'entry'
                if name == 'intro.md':
                    self.entry_type = 'intro'
                elif name == 'conclusions.md':
                    self.entry_type = 'conclusions'
                elif name == 'todos.md':
                    self.entry_type = 'todos'
                elif re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', name):
                    entry_date_data = name.strip('.md').split('-')[0:3]
                    year = int(entry_date_data[0])
                    month = int(entry_date_data[1])
                    day = int(entry_date_data[2])
                    entry_date = date(year, month, day)
                    self.entry_type = 'dated-entry'
                    self.date = entry_date
                self.content = processMD(self.uri)
            elif name == 'index.html':
                self.type = 'notebook_page'
            else:
                self.type = 'file'
                
            
        
    #create folder objects list
    #create file objects list
    
    folders = []
    found_files = []
    
    for item in os.walk(directory):
        
        root, dirs, files = item
        
        parsed_root = root.split('/')
        
        folder_name = parsed_root[-1]
        
        folder_root = '/'.join(parsed_root[:-1])
        
        folders.append(Folder(name = folder_name, root = folder_root))
        
        for file in files:
        
            file_name = file
            
            root = root
            new_file = File(name = file_name, root = root)
            found_files.append(new_file)
            
            
    for file in found_files:
        for folder in folders:
            if file.parent == folder.name:
                folder.files.append(file)
                #for file in folder.files:
                    #print file.name

    for folder in folders:
        found_dated_entry = False
        for file in folder.files:
            if found_dated_entry == False:
                if file.type == 'entry':
                    if file.entry_type == 'dated-entry':
                        print 'TRUE'
                        folder.makeExperiment()
                        found_dated_entry = True

    return(folders)
    
    #scan the folders for projects and experiments
    
    #scan the files for entries and process them accordingly and put them in
    
    #folders = []
    
    #files = []
    
    #entries = []
    
    #projects = []
    
    #experiments = []
    
treeScanner('/Users/christophermackay/Desktop/Coding/lab-notebook/notebook')
    