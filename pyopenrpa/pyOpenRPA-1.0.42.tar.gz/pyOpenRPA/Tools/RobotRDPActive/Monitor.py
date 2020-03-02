from pyOpenRPA.Robot import UIDesktop
from . import Connector
import os
import pdb
#Check for session is closed. Reopen if detected. Always keep session is active
def Monitor(inGlobalDict, inListUpdateTimeout):
    lFlagWhile = True
    while lFlagWhile:
        # UIOSelector list init
        lUIOSelectorList = []
        #Prepare selectors list for check
        for lIndex, lItem in enumerate(inGlobalDict["RDPList"]):
            lUIOSelectorList.append([{"title_re": f"{lItem['SessionHex']}.*", "backend": "win32"}])
        #Run wait command
        lRDPDissappearList = UIDesktop.UIOSelectorsSecs_WaitDisappear_List(lUIOSelectorList, inListUpdateTimeout)
        ###########################################
        #Analyze if flag safeturn off is activated
        if inGlobalDict.get("OrchestratorToRobotResetStorage",{}).get("SafeTurnOff",False):
            lFlagWhile=False
            #Set status disconnected for all RDP List
            for lItem in inGlobalDict["RDPList"]:
                lItem["FlagSessionIsActive"]=False
            #Kill all RDP sessions
            os.system('taskkill /F /im mstsc.exe')
            #Return from function
            return
        ###########################################
        ###########################################
        for lItem in lRDPDissappearList:
            inGlobalDict["RDPList"][lItem]["FlagSessionIsActive"] = False # Set flag that session is disconnected
            #pdb.set_trace()
            #Session start if it is not in ignore list
            #add check for selector if it is not in ignoreIndexList
            if lItem not in inGlobalDict["OrchestratorToRobotStorage"]["IgnoreIndexList"]:
                try:
                    Connector.Session(inGlobalDict["RDPList"][lItem])
                    inGlobalDict["RDPList"][lItem]["FlagSessionIsActive"] = True  # Flag that session is started
                except Exception:
                    pass
        ###########################################
        #Check if from Orchestrator full screen session is set
        if inGlobalDict["OrchestratorToRobotStorage"]["FullScreenSessionIndex"] != inGlobalDict["FullScreenSessionIndex"]:
            #Do some switches
            #If full screen mode we have now
            if inGlobalDict["FullScreenSessionIndex"] is not None:
                if inGlobalDict["RDPList"][inGlobalDict["FullScreenSessionIndex"]]["FlagSessionIsActive"]:
                    Connector.SessionScreen100x550(inGlobalDict["RDPList"][inGlobalDict["FullScreenSessionIndex"]]["SessionHex"])
            #If new session is setted
            if inGlobalDict["OrchestratorToRobotStorage"]["FullScreenSessionIndex"] is not None:
                if inGlobalDict["RDPList"][inGlobalDict["OrchestratorToRobotStorage"]["FullScreenSessionIndex"]]["FlagSessionIsActive"]:
                    Connector.SessionScreenFull(inGlobalDict["RDPList"][inGlobalDict["OrchestratorToRobotStorage"]["FullScreenSessionIndex"]]["SessionHex"])
            #Set one to other equal
            inGlobalDict["FullScreenSessionIndex"] = inGlobalDict["OrchestratorToRobotStorage"]["FullScreenSessionIndex"]
    return None
#TODO Def garbage window cleaner (if connection was lost)