import json
#ControlPanelDict
from desktopmagic.screengrab_win32 import (
	getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
	getRectAsImage, getDisplaysAsImages)
def Monitor_ControlPanelDictGet(inRequest,inGlobalDict):
    inResponseDict = inRequest.OpenRPAResponseDict
    # Create result JSON
    lResultJSON = {"RenderRobotList": []}
    lRenderFunctionsRobotList = inGlobalDict["ControlPanelDict"]["RobotList"]
    for lItem in lRenderFunctionsRobotList:
        # Выполнить вызов и записать результат
        lItemResultDict = lItem["RenderFunction"](inGlobalDict)
        # RunFunction
        lResultJSON["RenderRobotList"].append(lItemResultDict)
    # Send message back to client
    message = json.dumps(lResultJSON)
    # Write content as utf-8 data
    inResponseDict["Body"] = bytes(message, "utf8")

def GetScreenshot(inRequest,inGlobalDict):
    # Get Screenshot
    def SaveScreenshot(inFilePath):
        # grab fullscreen
        # Save the entire virtual screen as a PNG
        lScreenshot = getScreenAsImage()
        lScreenshot.save('screenshot.png', format='png')
        # lScreenshot = ScreenshotSecondScreen.grab_screen()
        # save image file
        # lScreenshot.save('screenshot.png')
    # Сохранить файл на диск
    SaveScreenshot("Screenshot.png")
    lFileObject = open("Screenshot.png", "rb")
    # Write content as utf-8 data
    inRequest.OpenRPAResponseDict["Body"] = lFileObject.read()
    # Закрыть файловый объект
    lFileObject.close()
def SettingsUpdate(inGlobalConfiguration):
    import os
    import pyOpenRPA.Orchestrator
    lOrchestratorFolder = "\\".join(pyOpenRPA.Orchestrator.__file__.split("\\")[:-1])
    lURLList = \
        [ #List of available URLs with the orchestrator server
            #{
            #    "Method":"GET|POST",
            #    "URL": "/index", #URL of the request
            #    "MatchType": "", #"BeginWith|Contains|Equal|EqualCase",
            #    "ResponseFilePath": "", #Absolute or relative path
            #    "ResponseFolderPath": "", #Absolute or relative path
            #    "ResponseContentType": "", #HTTP Content-type
            #    "ResponseDefRequestGlobal": None #Function with str result
            #}
            #Orchestrator basic dependencies
            {"Method":"GET", "URL": "/", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "Web\\Index.xhtml"), "ResponseContentType": "text/html"},
            {"Method":"GET", "URL": "/3rdParty/Semantic-UI-CSS-master/semantic.min.css", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\semantic.min.css"), "ResponseContentType": "text/css"},
            {"Method":"GET", "URL": "/3rdParty/Semantic-UI-CSS-master/semantic.min.js", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\semantic.min.js"), "ResponseContentType": "application/javascript"},
            {"Method":"GET", "URL": "/3rdParty/jQuery/jquery-3.1.1.min.js", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "..\\Resources\\Web\\jQuery\\jquery-3.1.1.min.js"), "ResponseContentType": "application/javascript"},
            {"Method":"GET", "URL": "/3rdParty/Google/LatoItalic.css", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "..\\Resources\\Web\\Google\\LatoItalic.css"), "ResponseContentType": "font/css"},
            {"Method":"GET", "URL": "/3rdParty/Semantic-UI-CSS-master/themes/default/assets/fonts/icons.woff2", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "..\\Resources\\Web\\Semantic-UI-CSS-master\\themes\\default\\assets\\fonts\\icons.woff2"), "ResponseContentType": "font/woff2"},
            {"Method":"GET", "URL": "/favicon.ico", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "Web\\favicon.ico"), "ResponseContentType": "image/x-icon"},
            {"Method":"GET", "URL": "/3rdParty/Handlebars/handlebars-v4.1.2.js", "MatchType": "EqualCase", "ResponseFilePath": os.path.join(lOrchestratorFolder, "..\\Resources\\Web\\Handlebars\\handlebars-v4.1.2.js"), "ResponseContentType": "application/javascript"},
            {"Method": "GET", "URL": "/Monitor/ControlPanelDictGet", "MatchType": "Equal", "ResponseDefRequestGlobal": Monitor_ControlPanelDictGet, "ResponseContentType": "application/json"},
            {"Method": "GET", "URL": "/GetScreenshot", "MatchType": "BeginWith", "ResponseDefRequestGlobal": GetScreenshot, "ResponseContentType": "image/png"}
        ]
    inGlobalConfiguration["Server"]["URLList"]=inGlobalConfiguration["Server"]["URLList"]+lURLList
    return inGlobalConfiguration