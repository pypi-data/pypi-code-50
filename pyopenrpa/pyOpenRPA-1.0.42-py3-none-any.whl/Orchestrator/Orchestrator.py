import subprocess
import json
import datetime
import time
import codecs
import os
import signal
import sys #Get input argument
import pdb
from . import Server
from . import Timer
from . import Processor
import logging
import copy
#from .Settings import Settings
import importlib
from importlib import util

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
#mGlobalDict = Settings.Settings(sys.argv[1])
Processor.mGlobalDict = mGlobalDict
Timer.mGlobalDict = mGlobalDict
Timer.Processor.mGlobalDict = mGlobalDict
Server.mGlobalDict = mGlobalDict
Server.Processor.mGlobalDict = mGlobalDict

#Инициализация настроечных параметров
lDaemonLoopSeconds=mGlobalDict["Scheduler"]["ActivityTimeCheckLoopSeconds"]
lDaemonActivityLogDict={} #Словарь отработанных активностей, ключ - кортеж (<activityType>, <datetime>, <processPath || processName>, <processArgs>)
lDaemonStartDateTime=datetime.datetime.now()

#Инициализация сервера
lThreadServer = Server.RobotDaemonServer("ServerThread", mGlobalDict)
lThreadServer.start()
#Logging
mGlobalDict["Logger"].info("Scheduler loop init")
#Вечный цикл
while True:
    lCurrentDateTime = datetime.datetime.now()
    #Циклический обход правил
    lFlagSearchActivityType=True
    for lIndex, lItem in enumerate(mGlobalDict["Scheduler"]["ActivityTimeList"]):
        #Проверка дней недели, в рамках которых можно запускать активность
        lItemWeekdayList=lItem.get("WeekdayList", [0, 1, 2, 3, 4, 5, 6])
        if lCurrentDateTime.weekday() in lItemWeekdayList:
            if lFlagSearchActivityType:
                #Лог
                lItemCopy = copy.deepcopy(lItem)
                lItemCopy["DateTimeUTCStringStart"]=datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%dT%H:%M:%S.%f")
                mGlobalDict["Scheduler"]["LogList"].append(lItemCopy)
                #######################################################################
                #Branch 1 - if has TimeHH:MM
                #######################################################################
                if "TimeHH:MM" in lItem:
                    #Вид активности - запуск процесса
                    #Сформировать временной штамп, относительно которого надо будет проверять время
                    #часовой пояс пока не учитываем
                    lActivityDateTime=datetime.datetime.strptime(lItem["TimeHH:MM"],"%H:%M")
                    lActivityDateTime=lActivityDateTime.replace(year=lCurrentDateTime.year,month=lCurrentDateTime.month,day=lCurrentDateTime.day)
                    #Убедиться в том, что время наступило
                    if (
                            lActivityDateTime>=lDaemonStartDateTime and
                            lCurrentDateTime>=lActivityDateTime and
                            (lIndex,lActivityDateTime) not in lDaemonActivityLogDict):
                        #Выполнить операцию
                        #Запись в массив отработанных активностей
                        lDaemonActivityLogDict[(lIndex,lActivityDateTime)]={"ActivityStartDateTime":lCurrentDateTime}
                        #Запустить процесс
                        Processor.ActivityListOrDict(lItem["Activity"])
                #######################################################################
                #Banch 2 - if TimeHH:MMStart, TimeHH:MMStop, ActivityIntervalSeconds
                #######################################################################
                if "TimeHH:MMStart" in lItem and "TimeHH:MMStop" in lItem and "ActivityIntervalSeconds" in lItem:
                    #Сформировать временной штамп, относительно которого надо будет проверять время
                    #часовой пояс пока не учитываем
                    lActivityDateTime=datetime.datetime.strptime(lItem["TimeHH:MMStart"],"%H:%M")
                    lActivityDateTime=lActivityDateTime.replace(year=lCurrentDateTime.year,month=lCurrentDateTime.month,day=lCurrentDateTime.day)
                    lActivityTimeEndDateTime=datetime.datetime.strptime(lItem["TimeHH:MMStop"],"%H:%M")
                    lActivityTimeEndDateTime=lActivityTimeEndDateTime.replace(year=lCurrentDateTime.year,month=lCurrentDateTime.month,day=lCurrentDateTime.day)
                    #Убедиться в том, что время наступило
                    if (
                            lCurrentDateTime<lActivityTimeEndDateTime and
                            lCurrentDateTime>=lActivityDateTime and
                            (lIndex,lActivityDateTime) not in lDaemonActivityLogDict):
                        #Запись в массив отработанных активностей
                        lDaemonActivityLogDict[(lIndex,lActivityDateTime)]={"ActivityStartDateTime":lCurrentDateTime}
                        #Запуск циклической процедуры
                        Timer.activityLoopStart(lItem["ActivityIntervalSeconds"], lActivityTimeEndDateTime, lItem["Activity"])
    #Уснуть до следующего прогона
    time.sleep(lDaemonLoopSeconds)