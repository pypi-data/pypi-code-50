#Import parent folder to import current / other packages
from pyOpenRPA.Robot import UIDesktop #Lib to access RDP window
import os #os for process run
import uuid #temp id for Template.rdp
import tempfile #Temporary location
import time
import subprocess
#Connect to RDP session
"""
{
    "Host": "", #Host address
    "Port": "", #RDP Port
    "Login": "", # Login
    "Password": "", #Password
    "Screen": {
        "Resolution":"FullScreen", #"640x480" or "1680x1050" or "FullScreen". If Resolution not exists set full screen
        "FlagUseAllMonitors": False, # True or False
        "DepthBit":"" #"32" or "24" or "16" or "15"
    }
}
"""
def Session(inRDPSessionConfiguration):
    #RDPConnector.SessionConnect(mConfiguration)
    #RDPConnector.LoginPassSet("111.222.222.111","ww","dd")
    (lRDPFile, lSessionHex) = SessionConfigurationCreate(inRDPSessionConfiguration)
    #Set session hex in globalDict
    inRDPSessionConfiguration["SessionHex"] = lSessionHex
    #Set login/password
    SessionLoginPasswordSet(inRDPSessionConfiguration["Host"],inRDPSessionConfiguration["Login"],inRDPSessionConfiguration["Password"])
    #Start session
    SessionRDPStart(lRDPFile)
    #Remove temp file
    time.sleep(4) #Delete file after some delay - one way to delete and run the RDP before because RDP is not read file in one moment
    os.remove(lRDPFile) # delete the temp rdp
    return inRDPSessionConfiguration
#Add login/ password to the windows credentials to run RDP
def SessionLoginPasswordSet(inHost, inLogin, inPassword):
    #Clear old login/password if it exists
    #os.system(f"cmdkey /delete:TERMSRV/{inHost}") #Dont need to delete because new user password will clear the previous creds
    #Set login password for host
    os.system(f"cmdkey /generic:TERMSRV/{inHost} /user:{inLogin} /pass:{inPassword}")
    return None
#Create current .rdp file with settings
#Return (full path to file, session hex)
def SessionConfigurationCreate(inConfiguration):
    #RobotRDPActive folder path
    lFileFullPath=__file__
    lFileFullPath = lFileFullPath.replace("/","\\")
    lRobotRDPActiveFolderPath = "\\".join(lFileFullPath.split("\\")[:-1])
    #Full path to Template.rdp file
    lRDPTemplateFileFullPath = os.path.join(lRobotRDPActiveFolderPath, "Template.rdp")
    #Open template file (.rdp encoding is USC-2 LE BOM = UTF-16 LE) http://qaru.site/questions/7156020/python-writing-a-ucs-2-little-endian-utf-16-le-file-with-bom
    lRDPTemplateFileContent = open(lRDPTemplateFileFullPath, "r", encoding="utf-16-le").read()
    #Prepare host:port
    lHostPort=inConfiguration['Host']
    if 'Port' in inConfiguration:
        if inConfiguration['Port']:
            lHostPort=f"{lHostPort}:{inConfiguration['Port']}"
    #Replace {Width}, {Height}, {BitDepth}, {HostPort}, {Login}
    lRDPTemplateFileContent = lRDPTemplateFileContent.replace("{Width}", str(inConfiguration.get('Screen',{}).get("Width",1680)))
    lRDPTemplateFileContent = lRDPTemplateFileContent.replace("{Height}", str(inConfiguration.get('Screen',{}).get("Height",1050)))
    lRDPTemplateFileContent = lRDPTemplateFileContent.replace("{BitDepth}", inConfiguration.get('Screen',{}).get("DepthBit","32"))
    lRDPTemplateFileContent = lRDPTemplateFileContent.replace("{HostPort}", lHostPort)
    lRDPTemplateFileContent = lRDPTemplateFileContent.replace("{Login}", inConfiguration['Login'])
    #Save template to temp file
    lRDPCurrentFileFullPath = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4().hex}.rdp")
    open(lRDPCurrentFileFullPath, "w", encoding="utf-16-le").write(lRDPTemplateFileContent)
    #Return .rdp full path
    return (lRDPCurrentFileFullPath, (lRDPCurrentFileFullPath.split("\\")[-1])[0:-4])
#RDPSessionStart
def SessionRDPStart(inRDPFilePath):
    #run rdp session
    lItemArgs = [inRDPFilePath]
    subprocess.Popen(lItemArgs, shell=True)
    #Wait for UAC unknown publisher exists
    lRDPFileName = (inRDPFilePath.split("\\")[-1])[0:-4]
    lWaitResult = UIDesktop.UIOSelectorsSecs_WaitAppear_List(
        [
            [{"title": "Подключение к удаленному рабочему столу", "class_name": "#32770", "backend": "win32"},
             {"title": "Боль&ше не выводить запрос о подключениях к этому компьютеру", "friendly_class_name": "CheckBox"}],
            [{"title": "Remote Desktop Connection", "class_name": "#32770", "backend": "win32"},
             {"title": "D&on't ask me again for connections to this computer",
              "friendly_class_name": "CheckBox"}],
            [{"title_re": f"{lRDPFileName}.*",
              "class_name": "TscShellContainerClass", "backend": "win32"}]
        ],
        30
    )
    #Click if 0 is appear (RUS)
    if 0 in lWaitResult:
        #Check the box do not retry
        UIDesktop.UIOSelector_Get_UIO([{"title": "Подключение к удаленному рабочему столу", "backend": "win32"},
             {"title": "Боль&ше не выводить запрос о подключениях к этому компьютеру", "friendly_class_name": "CheckBox"}]).check()
        #Go to connection
        UIDesktop.UIOSelector_Get_UIO([{"title": "Подключение к удаленному рабочему столу", "backend": "win32"},
             {"title":"Подкл&ючить", "class_name":"Button"}]).click()
        lWaitResult = UIDesktop.UIOSelectorsSecs_WaitAppear_List(
            [
                [{"title_re": f"{lRDPFileName}.*",
                  "class_name": "TscShellContainerClass", "backend": "win32"}]
            ],
            30
        )
    # Click if 1 is appear (ENG)
    if 1 in lWaitResult:
        # Check the box do not retry
        UIDesktop.UIOSelector_Get_UIO([{"title": "Remote Desktop Connection", "class_name": "#32770", "backend": "win32"},
             {"title": "D&on't ask me again for connections to this computer",
              "friendly_class_name": "CheckBox"}]).check()
        # Go to connection
        UIDesktop.UIOSelector_Get_UIO([{"title": "Remote Desktop Connection", "class_name": "#32770", "backend": "win32"},
                                       {"title": "Co&nnect", "class_name": "Button"}]).click()
        lWaitResult = UIDesktop.UIOSelectorsSecs_WaitAppear_List(
            [
                [{"title_re": f"{lRDPFileName}.*",
                  "class_name": "TscShellContainerClass", "backend": "win32"}]
            ],
            30
        )
    #Prepare little window
    SessionScreen100x550(lRDPFileName)
    return None
#Set fullscreen for app
def SessionScreenFull(inSessionHex):
    #Prepare little window
    lRDPWindow = UIDesktop.UIOSelector_Get_UIO([{"title_re": f"{inSessionHex}.*", "backend": "win32"}])
    lRDPWindow.maximize()
    lRDPWindow.set_focus()
    return None
#Set Little window of the session
def SessionScreen100x550(inSessionHex):
    #Prepare little window
    lRDPWindow = UIDesktop.UIOSelector_Get_UIO([{"title_re": f"{inSessionHex}.*", "backend": "win32"}])
    lRDPWindow.restore()
    lRDPWindow.move_window(10,10,550,100)
    return None
