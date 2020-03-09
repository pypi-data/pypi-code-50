#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class Computers:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##Computers
    def listComputers(self, expand=None, overrides=None):
        params = {}
        if expand:
            params['expand'] = expand
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers', params=params)
    def describeComputer(self, id, expand=None, overrides=None):
        params = {}
        if expand:
            params['expand'] = expand
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id), params=params)
    def modifyComputer(self, id, expand=None, overrides=None, payload=None):
        params = {}
        if expand:
            params['expand'] = expand
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id), data=payload, params=params)
    def deleteComputer(self, id):
        return self._connection.delete(url='/computers/' + str(id))
    def describeComputerSetting(self, id, setting, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/settings/' + str(setting), params=params)
    def modifyComputerSetting(self, id, setting, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/settings/' + setting, data=payload, params=params)
    def resetComputerSetting(self, id, setting, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/settings/' + setting, params=params)
    def createComputer(self, expand=None, overrides=None, payload=None):
        params = {}
        if expand:
            params['expand'] = expand
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers' , data=payload, params=params)
    def searchComputer(self, expand=None, overrides=None, payload=None):
        url = '/computers/search'
        computers = None
        params = {}
        if expand:
            params['expand'] = expand
        if overrides:
            params['overrides'] = overrides
        rtv = self._connection.post(url=url, data=payload, params=params)
        if 'computers' not in rtv:
            return rtv
        computers = rtv['computers']
        while len(rtv['computers']) > 0:
            if 'idTest' in payload['searchCriteria']:
                if payload['searchCriteria']['idTest'] == 'equal'  or payload['searchCriteria']['idTest'] == 'not-equal':
                    return computers
                if payload['searchCriteria']['idTest'] == 'greater-than-or-equal':
                    payload['searchCriteria']['idValue'] = int(computers[len(computers) - 1]['ID'])+1
                if payload['searchCriteria']['idTest'] == 'less-than-or-equal':
                    payload['searchCriteria']['idValue'] = int(computers[len(computers)-1]['ID'])-1
                if payload['searchCriteria']['idTest'] == 'less-than' or payload['searchCriteria']['idTest'] == 'greater-than':
                    payload['searchCriteria']['idValue'] = int(computers[len(computers) - 1]['ID'])
            rtv = self._connection.post(url=url, data=payload, params=params)
            computers.extend(rtv['computers'])
        return computers


    ##Computers Firewall Rule Assignments
    def listComputerFirewallAssignment(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/firewall/assignments', params=params)
    def addComputerFirewallAssignment(self, id, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/firewall/assignments', data=payload, params=params)
    def setComputerFirewallAssignment(self, id, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.put(url='/computers/' + str(id) + '/firewall/assignments', data=payload, params=params)
    def deleteComputerFirewallAssignment(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/firewall/assignments/'+ruleID, params=params)
    ##Computers Firewall Rule
    def listComputerFirewallRules(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/firewall/rules', params=params)
    def describeComputerFirewallRules(self, id, firewallRuleId, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/firewall/rules/'+firewallRuleId, params=params)
    def modifyComputerFirewallRules(self, id, firewallRuleId, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/firewall/rules/'+firewallRuleId, data=payload, params=params)
    def resetComputerFirewallRules(self, id, firewallRuleId, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/firewall/rules/'+firewallRuleId, params=params)
    #IntegrityMonitoring
    def listComputerIntegrityMonitoringRules(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/integritymonitoring/rules', params=params)
    def describeComputerIntegrityMonitoringRules(self, id, fintegritymonitoringlRuleId, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/integritymonitoring/rules/' + str(fintegritymonitoringlRuleId), params=params)
    def modifyComputerIntegrityMonitoringRules(self, id, fintegritymonitoringlRuleId, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/integritymonitoring/rules/' + str(fintegritymonitoringlRuleId), data=payload, params=params)
    def deleteComputerIntegrityMonitoringRules(self, id, fintegritymonitoringlRuleId, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/integritymonitoring/rules/' + str(fintegritymonitoringlRuleId), params=params)
    #Intrusion Prevention - assignments
    def listComputerIntrusionPreventionAssignment(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/assignments', params=params)
    def assignComputerIntrusionPreventionAssignment(self, id, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/intrusionprevention/assignments', data=payload, params=params)
    def setComputerIntrusionPreventionAssignment(self, id, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.put(url='/computers/' + str(id) + '/intrusionprevention/assignments', data=payload, params=params)
    def deleteComputerIntrusionPreventionAssignment(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/intrusionprevention/assignments/'+str(ruleID), params=params)
    #Intrusion Prevention - application type
    def listComputerIntrusionPreventionApplicationTypes(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes', params=params)
    def describeComputerIntrusionPreventionApplicationTypes(self, id, intrusionPreventionApplicationTypesId, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes/'+ str(intrusionPreventionApplicationTypesId), params=params)
    def modifyComputerIntrusionPreventionApplicationTypes(self, id, intrusionPreventionApplicationTypesId, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes/' + str(intrusionPreventionApplicationTypesId), data=payload, params=params)
    def deleteComputerIntrusionPreventionApplicationTypes(self, id, intrusionPreventionApplicationTypesId, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/intrusionprevention/applicationtypes/' + str(intrusionPreventionApplicationTypesId), params=params)
    #Intrusion Prevention - Rule
    def listComputerIntrusionPreventionRules(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/rules', params=params)
    def describeComputerIntrusionPreventionRule(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/intrusionprevention/rules/'+ str(ruleID), params=params)
    def modifyComputerIntrusionPreventionRule(self, id, ruleID, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/intrusionprevention/rules/' + str(ruleID), data=payload, params=params)
    def deleteComputerIntrusionPreventionRules(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/intrusionprevention/rules/' + str(ruleID), params=params)
    #Log Inspection assignment
    def listComputerLogInspectionAssignment(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/loginspection/assignments', params=params)
    def assignComputerLogInspectionAssignment(self, id, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/loginspection/assignments', params=params, data=payload)
    def setComputerLogInspectionAssignment(self, id, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.put(url='/computers/' + str(id) + '/loginspection/assignments', params=params, data=payload)
    def deleteComputerLogInspectionAssignment(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/loginspection/assignments/'+str(ruleID), params=params)
    #ILog Inspection  - rules
    def listComputerLogInspectionRules(self, id, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/loginspection/rules', params=params)
    def describeComputerLogInspectionRule(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.get(url='/computers/' + str(id) + '/loginspection/rules/' + str(ruleID), params=params)
    def modifyComputerLogInspectionRule(self, id, ruleID, overrides=None, payload=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.post(url='/computers/' + str(id) + '/loginspection/rules/' + str(ruleID), data=payload, params=params)
    def deleteComputerLogInspectionRule(self, id, ruleID, overrides=None):
        params = {}
        if overrides:
            params['overrides'] = overrides
        return self._connection.delete(url='/computers/' + str(id) + '/loginspection/rules/' + str(ruleID), params=params)



