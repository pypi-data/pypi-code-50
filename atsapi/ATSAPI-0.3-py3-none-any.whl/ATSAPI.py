import requests
import json
import base64

class ATSalarm:
    def __init__(self, alarmIP, alarmPort, alarmCode, alarmPin):
        #init variables
        self.alarmIP = alarmIP
        self.alarmPort = alarmPort
        self.alarmCode = alarmCode
        self.alarmPin = alarmPin
        self.server = 'https://security.syca.nl/'
        self.lastMessage = {}
        self.zoneStates = {}

        #making initial data dict
        self.data={'alarmIP':self.alarmIP,'alarmPort':self.alarmPort,'alarmCode':self.alarmCode,'alarmPin':self.alarmPin,'task':''}

        self.Connect()


    def Connect(self, task="servercheck", zone=""):
        self.data['task'] = task

        if zone == "":
            r = requests.post(self.server, data=self.data, verify=False)
            self.koekjes = r.cookies
            self.lastMessage = json.loads(r.text)
            print (self.lastMessage)
            self.status()
        else:
            # localData to append area
            localData = self.data
            localData["area"] = zone

            r = requests.post(self.server, data=localData, verify=False)
            self.koekjes = r.cookies
            self.lastMessage = json.loads(r.text)
            print (self.lastMessage)




    def status(self):
        # set task
        task = 'status'
        self.data['task'] = task

        # keep reconnecting till all data is retrieved
        #print(self.lastMessage)
        while "reconnect" in self.lastMessage:
            if self.lastMessage["reconnect"]:
                r = requests.post(self.server, data=self.data, verify=False, cookies=self.koekjes)
                self.lastMessage = json.loads(r.text)
                #print(self.lastMessage)

                if "messages" in self.lastMessage:
                    for message in self.lastMessage["messages"]:
                        if message["type"] == "data":
                            if message["status"] == "areaButtons":
                                self.zoneStates = json.loads(base64.standard_b64decode(message["code"]))
                                print(self.zoneStates)
                                print("amount of zones: " + str(len(self.zoneStates)))
                                for zone in self.zoneStates:
                                    if zone["status"] == 1:
                                        print(zone["name"] + " not armed")
                                    else:
                                        print(zone["name"] + " armed")

            else:
                break

    def arm(self, zone):
        self.Connect(task="areaon", zone=zone)

    def disarm(self, zone):
        self.Connect(task="areaoff", zone=zone)