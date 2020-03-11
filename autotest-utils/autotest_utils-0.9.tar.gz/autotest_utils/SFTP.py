import pysftp
import fnmatch
import os
ERROR_CODE=-1
class SFTP(pysftp.Connection):

    def __init__(self, host, port=None, login=None, password=None, private_key=None):
        super().__init__(host,port=port,username=login,password=password,private_key=private_key)

    def putFiles(self,masks,local,remote):
        with self.cd(remote):  # temporarily cd to remote
            for file in os.listdir(local):
                matched = any(fnmatch.fnmatch(file, mask) for mask in masks)
                if matched:
                    self.put(remotepath=remote+"/"+file,localpath=local+"/"+file)  # upload to remote

    def getFiles(self,masks,local,remote):
        for file in self.listdir(remote):
            matched = any(fnmatch.fnmatch(file, mask) for mask in masks)
            if matched:
                self.get(remotepath=remote + "/" + file, localpath=local + "/" + file)

    def fileList(self,mask,remote):
        filelist = []
        for file in self.listdir(remote):
            if (fnmatch.fnmatch(file, mask)):
                filelist.append(file)
        return filelist

    def clearDir(self,remote):
        for file in self.listdir(remote):
            self.remove(remote+'/'+file)

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass