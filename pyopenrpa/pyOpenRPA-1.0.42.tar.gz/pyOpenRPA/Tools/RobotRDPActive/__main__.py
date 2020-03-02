#Run example
#cd %~dp0..\..\Sources
#..\Resources\WPy64-3720\python-3.7.2.amd64\python.exe -m pyOpenRPA.Tools.RobotRDPActive "C:\Abs\Archive\scopeSrcUL\Settings.py"
#pause >nul
#Import parent folder to import current / other packages
#########################################################
import sys
import subprocess #start process async
import os #path, run, remove
import time #timer
import importlib
#lFolderPath = "\\".join(__file__.split("\\")[:-4])
lFolderPath = "/".join(__file__.split("/")[:-4])
sys.path.insert(0, lFolderPath)
#Единый глобальный словарь (За основу взять из Settings.py)
global mGlobalDict
#Call Settings function from argv[1] file
################################################
lSubmoduleFunctionName = "Settings"
lFileFullPath = sys.argv[1]
lModuleName = (lFileFullPath.split("\\")[-1])[0:-3]
lTechSpecification = importlib.util.spec_from_file_location(lModuleName, lFileFullPath)
lTechModuleFromSpec = importlib.util.module_from_spec(lTechSpecification)
lTechSpecificationModuleLoader = lTechSpecification.loader.exec_module(lTechModuleFromSpec)
mGlobalDict = None
if lSubmoduleFunctionName in dir(lTechModuleFromSpec):
    # Run SettingUpdate function in submodule
    mGlobalDict = getattr(lTechModuleFromSpec, lSubmoduleFunctionName)()
#################################################
#########################################################
from pyOpenRPA.Tools.RobotRDPActive import Connector
from pyOpenRPA.Tools.RobotRDPActive import Monitor
#Disable certificate warning
lCMDString = 'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Terminal Server Client" /v "AuthenticationLevelOverride" /t "REG_DWORD" /d 0 /f'
os.system(lCMDString)
#time.sleep()
for lConfigurationItem in mGlobalDict["RDPList"]:
    try:
        Connector.Session(lConfigurationItem)
        lConfigurationItem["FlagSessionIsActive"]=True #Flag that session is started
    except Exception:
        pass
#Run monitor
Monitor.Monitor(mGlobalDict, 1)
#Enable certificate warning
lCMDString = 'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Terminal Server Client" /v "AuthenticationLevelOverride" /t "REG_DWORD" /d 2 /f'
os.system(lCMDString)
#Close all thread from OrchestratorConnection
mGlobalDict["OrchestratorConnectorTerminateAll"]()