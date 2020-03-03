# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:45:32 2019

@author: Sam Jin Dou
"""
import os

def checkFolder(folderPath):
    if not os.path.isdir(folderPath):
        print("path: " + folderPath + "doesn't exist, and it is created")
        os.makedirs(folderPath)
		
class CStellarLog:
  
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
        
            
