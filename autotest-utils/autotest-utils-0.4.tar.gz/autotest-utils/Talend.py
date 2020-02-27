import shutil
import os
from subprocess import Popen,PIPE

ERROR_CODE=-1

def runTalendJob(scriptpath):
    if (shutil.which('java') is None): # check if java executable found in PATH
        print("Add path to java executable to PATH")
        return None
    my_env = os.environ.copy()
    p = Popen(scriptpath,env=my_env,stdout=PIPE,stderr=PIPE)
    stdout, stderr = p.communicate()
    if(stderr is b""):
        return 0,stdout.decode("utf-8"),None
    else:
        return ERROR_CODE, stdout.decode("utf-8"), stderr.decode("utf-8")
