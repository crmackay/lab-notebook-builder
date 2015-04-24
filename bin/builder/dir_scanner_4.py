import os
from datetime import date
from md_processor import EditHTML, processMD
import re
from collections import defaultdict

class Folder(object):
    """This is the folder Class
    """
    
    def __init__(self, name, root, dataFiles = None, entries = None):
        self.name = name
        self.root = root
        self.uri = os.path.join(root, name)
        self.dataFiles = dataFiles
        self.entries = entries
        self.parent = os.path.split(root)[1]
        self.children = []

class Experiment(Folder):
    def __init__(self, name, root, dataFiles = None, entries = None, startDate = None, endDate = None):
        Folder.__init__(self, name, root, dataFiles, entries)
        self.startDate = startDate
        self.endDate = endDate

class Project(Folder):
    def __init__(self, name, root, dataFiles = None, entries = None):
        Folder.__init__(self, name, root, dataFiles, entries)
        self.experiments = []
        for child in self.children:
            if type(child) is Experiment:
                self.experiments.append(child)
        self.experiments.sort(key = lambda x: x.startDate)
 
class File(object):
    def __init__(self, name, extension, root):
        self.name = name
        self.extension = extension
        self.root = root
        self.uri = root+'/' + name + extension
        self.parent = os.path.split(root)[1]

class DataFile(File):
    def __init__(self, name, extension, root):
        File.__init__(self, name, extension, root)
        self.lastModified = os.stat(self.uri).st_mtime
      
class Entry(File):
    def __init__(self, name, extension, root):
        File.__init__(self, name, extension, root)
        self.content = EditHTML(processMD(self.uri))
     
class Introduction(Entry):
    def __init__(self, name, extension, root):
        File.__init__(self, name, extension, root)
        ##parse metadata for use in the experiment

class Conclusion(Entry):
    def __init__(self, name, extension, root):
        File.__init__(self, name, extension, root)
        
class ToDos(Entry):
    def __init__(self, name, extension, root):
        File.__init__(self, name, extension, root)
        ##TODO create task objects and put them here

class DatedEntry(Entry):
    def __init__(self, name, entryDate, extension, root):
        File.__init__(self, name, extension, root)
        year, month, day = [int(x) for x in entryDate.split('-')]
        self.date = date(year, month, day)
        
def parseFile():
    pass

def treeScan(directory):
    
    folders = []
    
    for root, dirs, files in os.walk(directory):
    
        folderRoot, folderName = os.path.split(root)
        
        folderTitle, folderDate = parseFolderDate(folderName)
        
        foundDataFiles = []
        foundEntries = defaultdict(list)
        
        for file in files:
            fileName = os.path.splitext(file)[0]
            extension = os.path.splitext(file)[1]
            if extension == '.md':
                entryType = fileName
                date_search = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', fileName)
                
                if fileName == 'introduction':
                    newFile = Introduction(fileName, extension, root)
                
                elif fileName == 'conclusion':
                    newFile = Conclusion(fileName, extension, root)
                
                elif fileName == 'todos':
                    newFile = ToDos(fileName, extension, root)

                elif date_search:
                    date = fileName[date_search.start(0):date_search.end(0)]
                    fileName = fileName[date_search.end(0):]
                    if fileName > len(date):
                        newFile = DatedEntry(fileName, date, extension, root)
                
                foundEntries[entryType].append(newFile)
                
            elif fileName != 'index.html':
                newFile = DataFile(fileName, extension, root)
                foundDataFiles.append(newFile)
                
            else:
                # it IS index.html, and we w will leave it alone
                pass
        
        newFolder = Folder(name = folderName, root = folderRoot, 
                            dataFiles = foundDataFiles, entries = foundEntries)
        folders.append(newFolder)
    
    # scan directory making folder and file objects 
        # each file object can be specific
        # folder objects are generic
        
    # result : list of folder objects, each with a parent name, and set of included files
    
    # go through folder list
        # if its experiment make experiment
        # if its a project make a project
    
    # put folder parents and children into one another
    
    # 
    
    return(folders)
    
    #scan the folders for projects and experiments
    
    #scan the files for entries and process them accordingly and put them in
    
    #folders = []
    
    #files = []
    
    #entries = []
    
    #projects = []
    
    #experiments = []

if __name__ == '__main__':
    test_directory = '/Users/christophermackay/Desktop/Coding/lab-notebook/notebook'
    folders = treeScan(test_directory)
    for folder in folders:
        print folder.name
        print type(folder)
    

''' 
            
    def makeExperiment(self):
        newExperiment = Experiment(self.root, self.name)
        newExperiment.status = 'active'
        newExperiment.data = []
        #print self.entries
        file_list = newExperiment.files
        for file in file_list:
        #print file.name
        if file.type == 'entry':
            if file.entry_type == 'dated-entry':
            newExperiment.entries.append(file)
            elif file.entry_type == 'intro':
            newExperiment.intro = file
            elif file.entry_type == 'conclusions':
            newExperiment.conclusions = file
            newExperiment.status = 'completed'
            elif file.entry_type == 'todos':
            newExperiment.todos = file
        else:
            newExperiment.data.append(file)

        if newExperiment.entries is not None:
            newExperiment.entries.sort(key = lambda x: x.date)

        newExperiment.start = self.entries[0].date
        
        if newExperiment.status == 'completed':
            newExperiment.end = newExperiment.entries[-1].date
        else:
            newExperiment.status = 'active'

        return newExperiment
        
    def makeProject(self):
        newProject = Project(
        self.experiments = []
        self.type = 'project'
            
            
'''