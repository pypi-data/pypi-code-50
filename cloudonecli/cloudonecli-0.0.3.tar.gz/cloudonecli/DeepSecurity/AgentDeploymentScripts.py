#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class AgentDeploymentScripts:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection

    def generateAgentDeploymentScript(self, payload):
        return self._connection.send(url='/agentdeploymentscripts', data=payload)