#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class AgentVersionControl:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##AgentVersionControl
    def listAgentVersionControl(self, profileID):
        return self._connection.get(url='/agentversioncontrolprofiles/' + str(profileID) + '/agentversioncontrols')
    def modifyAgentVersionControl(self, profileID, payload):
        return self._connection.get(url='/agentversioncontrolprofiles/' + str(profileID) + '/agentversioncontrols', data=payload)
    def searchAgentVersionControl(self, profileID, payload):
        return self._connection.get(url='/agentversioncontrolprofiles/' + str(profileID) + '/agentversioncontrols/search', data=payload)
    def describeAgentVersionControl(self, profileID, agentVersionControlID):
        return self._connection.get(url='/agentversioncontrolprofiles/' + str(profileID) + '/agentversioncontrols/' + str(agentVersionControlID))
    def listAgentVersionControlProfiles(self):
        return self._connection.get(url='/agentversioncontrolprofiles')
    def describeAgentVersionControlProfiles(self, profileID):
        return self._connection.get(url='/agentversioncontrolprofiles/' + str(profileID))



