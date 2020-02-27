import pysftp
import fnmatch
import os
ERROR_CODE=-1

def putToSFTP(host,port,remote,login,password,privateKey,mask,local):
    try:
        sftp = pysftp.Connection(host=host,port=port, username=login, password=password,private_key=privateKey)
    except Exception as ex:
        return ERROR_CODE,ex
    else:
        with sftp.cd(remote):  # temporarily cd to remote
            for file in os.listdir(local):
                if(fnmatch.fnmatch(file,mask)):
                    sftp.put(remotepath=remote+"/"+file,localpath=local+"/"+file)  # upload to remote
        return 0, None

def getFromSFTP(host,port,remote,login,password,privateKey,mask,local):
    try:
        sftp = pysftp.Connection(host=host,port=port, username=login, password=password,private_key=privateKey)
    except Exception as ex:
        return ERROR_CODE,ex
    else:
        for file in sftp.listdir(remote):
            if (fnmatch.fnmatch(file, mask)):
                sftp.get(remotepath=remote + "/" + file, localpath=local + "/" + file)
        return 0,None
