#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class Computers:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##Computers
    def listComputers(self):
        return self._connection.get(url='/computers')
    def Computer(self, id):
        return self._connection.get(url='/computers/' + str(id))
    def modifyComputer(self, id, payload):
        return self._connection.send(url='/computers/' + str(id), data=payload)
    def deleteComputer(self, id):
        return self._connection.delete(url='/computers/' + str(id))
    def describeComputerSetting(self, id, setting):
        return self._connection.get(url='/computers/' + str(id) + '/settings/' + setting)
    def modifyComputerSetting(self, id, setting, payload):
        return self._connection.get(url='/computers/' + str(id) + '/settings/' + setting, data=payload)
    def resetComputerSetting(self, id, setting):
        return self._connection.delete(url='/computers/' + str(id) + '/settings/' + setting)
    def createComputer(self, payload):
        return self._connection.send(url='/computers' , data=payload)
    def searchComputer(self, payload, expand=None, overrides=False):
        url = '/computers/search'
        if expand is not None:
            url = url + "?expand=" + expand
        if overrides:
            if expand is None:
                url = url + "?overrides=True"
            else:
                url = url + ",overrides=True"
        return self._connection.send(url=url, data=payload)
    ##Computers Firewall Rule Assignments
    def describeComputerFirewallAssignment(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/firewall/assignments')
    def assignComputerFirewallAssignment(self, id, payload):
        return self._connection.send(url='/computers/' + str(id) + '/firewall/assignments', data=payload)
    def setComputerFirewallAssignment(self, id, payload):
        return self._connection.put(url='/computers/' + str(id) + '/firewall/assignments', data=payload)
    def deleteComputerFirewallAssignment(self, id, ruleID):
        return self._connection.delete(url='/computers/' + str(id) + '/firewall/assignments/'+ruleID)
    ##Computers Firewall Rule
    def listComputerFirewallRules(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/firewall/rules')
    def describeComputerFirewallRules(self, id, firewallRuleId):
        return self._connection.get(url='/computers/' + str(id) + '/firewall/rules/'+firewallRuleId)
    def modifyComputerFirewallRules(self, id, firewallRuleId, payload):
        return self._connection.send(url='/computers/' + str(id) + '/firewall/rules/'+firewallRuleId, data=payload)
    def deleteComputerFirewallRules(self, id, firewallRuleId):
        return self._connection.delete(url='/computers/' + str(id) + '/firewall/rules/'+firewallRuleId)
    #IntegrityMonitoring
    def listComputerIntegrityMonitoringRules(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/integritymonitoring/rules')
    def describeComputerIntegrityMonitoringRules(self, id, fintegritymonitoringlRuleId):
        return self._connection.get(url='/computers/' + str(id) + '/integritymonitoring/rules/' + str(fintegritymonitoringlRuleId))
    def modifyComputerIntegrityMonitoringRules(self, id, fintegritymonitoringlRuleId, payload):
        return self._connection.send(url='/computers/' + str(id) + '/integritymonitoring/rules/' + str(fintegritymonitoringlRuleId), data=payload)
    def deleteComputerIntegrityMonitoringRules(self, id, fintegritymonitoringlRuleId):
        return self._connection.delete(url='/computers/' + str(id) + '/integritymonitoring/rules/' + str(fintegritymonitoringlRuleId))
    #Intrusion Prevention - assignments
    def listComputerIntrusionPreventionAssignment(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/assignments')
    def assignComputerIntrusionPreventionAssignment(self, id, payload):
        return self._connection.send(url='/computers/' + str(id) + '/intrusionprevention/assignments', data=payload)
    def setComputerIntrusionPreventionAssignment(self, id, payload):
        return self._connection.put(url='/computers/' + str(id) + '/intrusionprevention/assignments', data=payload)
    def deleteComputerIntrusionPreventionAssignment(self, id, ruleID):
        return self._connection.delete(url='/computers/' + str(id) + '/intrusionprevention/assignments/'+str(ruleID))
    #Intrusion Prevention - application type
    def listComputerIntrusionPreventionApplicationTypes(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes')
    def describeComputerIntrusionPreventionApplicationTypes(self, id, intrusionPreventionApplicationTypesId):
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes/'+ str(intrusionPreventionApplicationTypesId))
    def modifyComputerIntrusionPreventionApplicationTypes(self, id, intrusionPreventionApplicationTypesId, payload):
        return self._connection.send(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes/' + str(intrusionPreventionApplicationTypesId), data=payload)
    def deleteComputerIntrusionPreventionApplicationTypes(self, id, intrusionPreventionApplicationTypesId):
        return self._connection.delete(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes/' + str(intrusionPreventionApplicationTypesId))
    #Intrusion Prevention - Rule
    def listComputerIntrusionPreventionRules(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/rules')
    def describeComputerIntrusionPreventionRules(self, id, ruleID):
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/rules/'+ str(ruleID))
    def modifyComputerIntrusionPreventionRules(self, id, ruleID, payload):
        return self._connection.send(url='/computers/' + str(id) + '/intrusionprevention/rules/' + str(ruleID), data=payload)
    def deleteComputerIntrusionPreventionRules(self, id, ruleID):
        return self._connection.delete(url='/computers/' + str(id) + '/intrusionprevention/rules/' + str(ruleID))
    #Log Inspection assignment
    def listComputerLogInspectionAssignment(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/loginspection/assignments')
    def assignComputerLogInspectionAssignment(self, id, payload):
        return self._connection.send(url='/computers/' + str(id) + '/loginspection/assignments', data=payload)
    def setComputerLogInspectionAssignment(self, id, payload):
        return self._connection.put(url='/computers/' + str(id) + '/loginspection/assignments', data=payload)
    def deleteComputerLogInspectionAssignment(self, id, ruleID):
        return self._connection.delete(url='/computers/' + str(id) + '/loginspection/assignments/'+str(ruleID))
    #ILog Inspection  - rules
    def listComputerLogInspectionRules(self, id):
        return self._connection.get(url='/computers/' + str(id) + '/loginspection/rules')
    def describeComputerLogInspectionRules(self, id, ruleID):
        return self._connection.get(url='/computers/' + str(id) + '/loginspection/rules/' + str(ruleID))
    def modifyComputerLogInspectionRules(self, id, ruleID, payload):
        return self._connection.send(url='/computers/' + str(id) + '/loginspection/rules/' + str(ruleID), data=payload)
    def deleteComputerLogInspectionRules(self, id, ruleID):
        return self._connection.delete(url='/computers/' + str(id) + '/loginspection/rules/' + str(ruleID))



