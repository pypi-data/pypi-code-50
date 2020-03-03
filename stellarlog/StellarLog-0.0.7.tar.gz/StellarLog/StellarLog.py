# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:45:32 2019

@author: Sam Jin Dou
"""
import os
from configparser import ConfigParser,BasicInterpolation

def checkFolder(folderPath):
    if not os.path.isdir(folderPath):
        print("path: " + folderPath + "doesn't exist, and it is created")
        os.makedirs(folderPath)

def loadBinFast(Dir):
    f = open(Dir,'rb')
    a = array.array('d')
    a.fromfile(f, os.path.getsize(Dir) // a.itemsize)
    return np.asarray(a)
    

def loadText(Dir):
    f=open(Dir, "r")
    contents = f.read()
    f.close()
    return contents
	
def getFileList(folder_path,extension):
    out = [folder_path+file for file in os.listdir(folder_path) if file.endswith(extension)]
    if(len(out)==0):
        print("getFileList's error: folder: '" + str(folder_path) + "'is empty with '" + str(extension) + "' kind of file")
        return -1
    else:
        return out
		
def getFileName(path):
    dataSetName, extension = os.path.splitext(os.path.basename(path))    
    return dataSetName    

def getSubFolderName(folder):
    subfolders = [f.name for f in os.scandir(folder) if f.is_dir() ]
    return subfolders
	
class CLog:
  
    def __init__(self,folder,Name):
        checkFolder(folder)
        self.fileName = folder+Name + '.txt'
        self.Open()
        self.save()
        self.folder = folder
        self.name = Name
    
    def Open(self):
        self.fileHandle = open(self.fileName, "a+")
        
    def record(self,log,newline:bool = True):
        if(type(log)==list):
            for j in log:
                self.fileHandle.write(str(j)+' ')
        elif(type(log) == str):
            self.fileHandle.write(log)
        else:
            print("Clog doesn't support this kind of log", type(log))
        
        if(newline == True):
            self.fileHandle.write('\n')
        else:
            self.fileHandle.write(' ')
        
    def openRecordSave(self,log,newline:bool = True):
        self.Open()
        self.record(log,newline)
        self.save()
    
    def safeRecordTime(self,log,newline:bool = True):
        self.openRecordSave(log + ', time: ' + str(datetime.datetime.now()),newline)
    
    def safeRecord(self,log,newline:bool = True):
        self.openRecordSave(log ,newline)
    
    def save(self):
        self.fileHandle.close()

class CDirectoryConfig:
    
    def __init__(self,dir_List, confFile):
        self.dir_dict = dict()
        self.confFile = confFile
        for i in dir_List:
            self.dir_dict[i] = ''
        self.load_conf()
            
    def load_conf(self):
        conf_file = self.confFile
        config = ConfigParser(interpolation=BasicInterpolation())
        config.read(conf_file,encoding = 'utf-8')
        conf_name = getFileName(conf_file)
        for dir_1 in self.dir_dict:
            self.dir_dict[dir_1] = config.get(conf_name, dir_1)
#            print(dir_1,config.get(conf_name, dir_1))
    
    def p(self,keyName):
        return self.dir_dict[keyName]
    
    def __getitem__(self,keyName):
        return self.dir_dict[keyName]
    
    def checkFolders(self,foldersList = None):
        if foldersList != None:
            pass
        else:
            foldersList = self.dir_dict.keys()
        
        for folder in foldersList:
                checkFolder(self.p(folder))
            
