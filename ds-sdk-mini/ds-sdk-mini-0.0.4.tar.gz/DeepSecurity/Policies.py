#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

#import connect
#import config

class Policies:
    def __init__(self, config, connection):
        self._config=config
        self._connection = connection
    ##Policies
    def listPolicies(self):
        return self._connection.get(url='/policies')
    def createPolicy(self, payload):
        return self._connection.send(url='/policies', data=payload)
    def Policy(self, id):
        return self._connection.get(url='/policies/' + str(id))
    def modifyPolicy(self, id, payload):
        return self._connection.send(url='/policies/' + str(id), data=payload)
    def deletePolicy(self, id):
        return self._connection.delete(url='/policies/' + str(id))
    def searchPolicies(self, overrides=False, payload=""):
        url = '/policies/search'
        if overrides:
            url = url + "?overrides=True"
        return self._connection.send(url=url, data=payload)
    # Default Policy Setting
    def describePolicyDefaultSetting(self, name):
        return self._connection.get(url='/policies/default/settings/' + str(name))
    def modifyPolicyDefaultSetting(self, name, payload):
        return self._connection.send(url='/policies/default/settings/' + str(name), data=payload)
    def deletePolicyDefaultSetting(self, name):
        return self._connection.delete(url='/policies/default/settings/' + str(name))
    #Default Policy
    def listPolicyDefault(self):
        return self._connection.get(url='/policies/default')
    def modifyPolicyDefault(self, payload):
        return self._connection.send(url='/policies/default', data=payload)
    def describePolicyDefault(self, policyID, name):
        return self._connection.get(url='/policies/' + policyID + '/settings/' + str(name))
    def modifyPolicySetting(self, policyID, name, payload):
        return self._connection.send(url='/policies/' + policyID + '/settings/' + str(name), data=payload)
    def resetPolicySetting(self, policyID, name):
        return self._connection.delete(url='/policies/' + policyID + '/settings/' + str(name))
    #Policy Firewall assignments
    def listPolicyFirewallRulesAssignments(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/firewall/assignments')
    def AddPolicyFirewallRuleAssignments(self, policyID, payload):
        return self._connection.send(url='/policies/' + policyID + '/firewall/assignments', data=payload)
    def SetPolicyFirewallRulesAssignments(self, policyID, payload):
        return self._connection.put(url='/policies/' + policyID + '/firewall/assignments', data=payload)
    def deletePolicyFirewallRuleAssignments(self, policyID, firewallID):
        return self._connection.delete(url='/policies/' + policyID + '/firewall/assignments/' + str(firewallID))
    # Policy Firewall
    def listPolicyFirewallRules(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/firewall/rules')
    def describePolicyFirewallRules(self, policyID, firewallID):
        return self._connection.get(url='/policies/' + policyID + '/firewall/rules/' + str(firewallID))
    def modifyPolicyFirewallRules(self, policyID, firewallID, payload):
        return self._connection.send(url='/policies/' + policyID + '/firewall/rules/' + str(firewallID), data=payload)
    def resetPolicyFirewallRules(self, policyID, firewallID):
        return self._connection.delete(url='/policies/' + policyID + '/firewall/rules/' + str(firewallID))
    # Integrity monitoring assignments
    def listPolicyIntegrityMonitoringRulesAssignments(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/integritymonitoring/assignments')
    def AddPolicyIntegrityMonitoringRuleAssignments(self, policyID, payload):
        return self._connection.send(url='/policies/' + policyID + '/integritymonitoring/assignments', data=payload)
    def SetPolicyIntegrityMonitoringRulesAssignments(self, policyID, payload):
        return self._connection.put(url='/policies/' + policyID + '/integritymonitoring/assignments', data=payload)
    def deletePolicyIntegrityMonitoringRuleAssignments(self, policyID, integritymonitoringID):
        return self._connection.delete(url='/policies/' + policyID + '/integritymonitoring/assignments/' + str(integritymonitoringID))
    # Integrity monitoring
    def listPolicyIntegrityMonitoringRules(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/integritymonitoring/rules')
    def describePolicyIntegrityMonitoringRules(self, policyID, integritymonitoringID):
        return self._connection.get(url='/policies/' + policyID + '/integritymonitoring/rules/' + str(integritymonitoringID))
    def modifyPolicyIntegrityMonitoringRules(self, policyID, integritymonitoringID, payload):
        return self._connection.send(url='/policies/' + policyID + '/integritymonitoring/rules/' + str(integritymonitoringID), data=payload)
    def resetPolicyIntegrityMonitoringRules(self, policyID, integritymonitoringID):
        return self._connection.delete(url='/policies/' + policyID + '/integritymonitoring/rules/' + str(integritymonitoringID))
    # Intrusion Prevention assignments
    def listPolicyIntrusionPreventionRulesAssignments(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/intrusionprevention/assignments')
    def AddPolicyIntrusionPreventionRuleAssignments(self, policyID, payload):
        return self._connection.send(url='/policies/' + policyID + '/intrusionprevention/assignments', data=payload)
    def SetPolicyIntrusionPreventionRulesAssignments(self, policyID, payload):
        return self._connection.put(url='/policies/' + policyID + '/intrusionprevention/assignments', data=payload)
    def deletePolicyIntrusionPreventionRuleAssignments(self, policyID, intrusionpreventionID):
        return self._connection.delete(url='/policies/' + policyID + '/intrusionprevention/assignments/' + str(intrusionpreventionID))
    # Intrusion Prevention
    def listPolicyIntrusionPreventionRules(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/intrusionprevention/rules')
    def describePolicyIntrusionPreventionRules(self, policyID, intrusionpreventionID):
        return self._connection.get(url='/policies/' + policyID + '/intrusionprevention/rules/' + str(intrusionpreventionID))
    def modifyPolicyIntrusionPreventionRules(self, policyID, intrusionpreventionID, payload):
        return self._connection.send(url='/policies/' + policyID + '/intrusionprevention/rules/' + str(intrusionpreventionID), data=payload)
    def resetPolicyIntrusionPreventionRules(self, policyID, intrusionpreventionID):
        return self._connection.delete(url='/policies/' + policyID + '/intrusionprevention/rules/' + str(intrusionpreventionID))
    # Intrusion Prevention application
    def listPolicyIntrusionPreventionApplication(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/intrusionprevention/applicationtypes')
    def describePolicyIntrusionPreventionApplication(self, policyID, applicationID):
        return self._connection.get(url='/policies/' + policyID + '/intrusionprevention/applicationtypes/' + str(applicationID))
    def modifyPolicyIntrusionPreventionApplication(self, policyID, applicationID, payload):
        return self._connection.send(url='/policies/' + policyID + '/intrusionprevention/applicationtypes/' + str(applicationID), data=payload)
    def resetPolicyIntrusionPreventionApplication(self, policyID, applicationID):
        return self._connection.delete(url='/policies/' + policyID + '/intrusionprevention/applicationtypes/' + str(applicationID))
    #Log inspection assignments
    def listPolicyLogInspectionRulesAssignments(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/loginspection/assignments')
    def AddPolicyLogInspectionRuleAssignments(self, policyID, payload):
        return self._connection.send(url='/policies/' + policyID + '/loginspection/assignments', data=payload)
    def SetPolicyLogInspectionRulesAssignments(self, policyID, payload):
        return self._connection.put(url='/policies/' + policyID + '/loginspection/assignments', data=payload)
    def deletePolicyLogInspectionRuleAssignments(self, policyID, loginspectionID):
        return self._connection.delete(url='/policies/' + policyID + '/loginspection/assignments/' + str(loginspectionID))
    #Log Inspection
    def listPolicyLogInspection(self, policyID):
        return self._connection.get(url='/policies/' + policyID + '/loginspection/rules')
    def describePolicyLogInspection(self, policyID, applicationD):
        return self._connection.get(url='/policies/' + policyID + '/loginspection/rules/' + str(applicationD))
    def modifyPolicyLogInspection(self, policyID, applicationD, payload):
        return self._connection.send(url='/policies/' + policyID + '/loginspection/rules/' + str(applicationD), data=payload)
    def resetPolicyLogInspection(self, policyID, loginspectionID):
        return self._connection.delete(url='/policies/' + policyID + '/loginspection/rules/' + str(loginspectionID))


