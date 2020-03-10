#!/usr/bin/env python3
import pyVim
import pyVmomi
from pyVmomi import vim
from pyVim.connect import SmartConnect,Disconnect
import requests
import os
import json
import logging
import socket
import atexit
import ssl
import time
from getmac import get_mac_address
from collections import namedtuple
from . log_exception import LogException
from . import global_vars

default_context = ssl._create_default_https_context
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings()
PROVIDER = "VMWare-VCenter"
class VmwareDetails:
   LogException = LogException()    
   def get_infra_details_for_report(self,config_dict):
       esxi_user = config_dict['esxi_user'].strip('\"')
       esxi_password = config_dict['esxi_password'].strip('\"')
       vc_User = config_dict['vsphere_user'].strip('\"').replace('\\\\','\\')
       vc_Password = config_dict['vsphere_password'].strip('\"')
       vcip = config_dict['vsphere_server'].strip('\"')
       dc_id = config_dict['vsphere_datacenter'].strip('\"')
       logging.debug('Getting VCenter infra details')
       infra_details = {}
       vc_session_id = self.get_session_id(vcip,vc_User,vc_Password)
       rsPool = self.get_rsPool_id(vcip,config_dict['vsphere_resource_pool'].strip('\"'),vc_session_id)
       esxi_details = self.get_esxi_details(vcip,vc_User,vc_Password,dc_id,esxi_user,esxi_password)
       vc_details = self.get_vc_details(vcip,vc_User,vc_Password)
       vm_details = self.get_vm_details(vcip,'', vc_session_id)
       infra_details['vc_details'] = vc_details
       infra_details['esxi_details'] = esxi_details
       infra_details['vm_details'] = vm_details
       self.del_session_id(vcip,vc_session_id)
       return infra_details

   def get_vc_details(self, vcip, vc_User, vc_Password):
       try:
          logging.debug('Getting vCenter details')
          vc_details = {}
          vc_con = SmartConnect(host=vcip, user=vc_User, pwd=vc_Password)
          content = vc_con.RetrieveContent()
          vc_details['name'] = content.about.name
          vc_details['version'] = content.about.version
          vc_details['apiVer'] = content.about.apiVersion
          vc_details['hyperVisor'] = content.about.build
          atexit.register(Disconnect, vc_con)
          return vc_details
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting vCenter details : ' + str(e))


   def get_esxi_details(self, vcip, vc_User, vc_Password, dc_id,esxi_user,esxi_password):
       try:
           logging.debug('Getting esxi details')
           host = {}
           host_details = []
           si = SmartConnect(host=vcip, user=vc_User, pwd=vc_Password)
           content = si.RetrieveContent()        
           objview = content.viewManager.CreateContainerView(content.rootFolder, [vim.Datacenter],True)
           dcList = objview.view
           objview.Destroy()
           for dc in dcList:
              if(dc.name==dc_id):
                 for cluster in dc.hostFolder.childEntity:
                    for hostObj in cluster.host:
                       host['name'] = hostObj.name
                       host['ipaddress'] = socket.gethostbyname(hostObj.name)
                       for i in range(len(hostObj.hardware.systemInfo.otherIdentifyingInfo)):
                          if ('ServiceTag' in hostObj.hardware.systemInfo.otherIdentifyingInfo[i].identifierType.key):
                             host['serviceTag'] = hostObj.hardware.systemInfo.otherIdentifyingInfo[i].identifierValue
                    
                       host['biosVer'] = hostObj.hardware.biosInfo.biosVersion
                       hostCon = SmartConnect(host=host['ipaddress'],user=esxi_user,pwd=esxi_password)
                       host['hyperVisor'] = hostCon.RetrieveContent().about.build
                       host_details.append(host.copy())
                       atexit.register(Disconnect, hostCon)
           return host_details
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting esxi details : ' + str(e))

   def get_vm_details(self,vcip,rsPool,vc_session_id):
       try:
           logging.debug('Getting VM details')
           vm_details = []
           vms_url = 'https://{0}/rest/vcenter/vm?filter.power_states.1=POWERED_ON&filter.power_states.1=POWERED_OFF&filter.resource_pools.1={1}'.format(vcip,rsPool)
           #vms_url = 'https://{0}/rest/vcenter/vm?filter.resource_pools.1={1}'.format(vcip,rsPool)
           response = requests.get(vms_url, verify=False, headers={"vmware-api-session-id": vc_session_id})
           for dict in response.json()['value']:
               if('vm' in dict):
                   vm = {}
                   vm['hostname'] = dict['name']
                   vm_id = dict['vm']
                   vmip_url = 'https://{0}/rest/vcenter/vm/{1}/guest/identity'.format(vcip,vm_id)
                   vmip_response = requests.get(vmip_url, verify=False, headers={"vmware-api-session-id": vc_session_id})
                   vm_mac_response = requests.get('https://{0}/rest/vcenter/vm/{1}'.format(vcip,vm_id), verify=False, headers={"vmware-api-session-id": vc_session_id})
                   if 'ip_address' in vmip_response.json()['value']:
                       vm['ip_address'] = vmip_response.json()['value']['ip_address']
                       vm['os'] = vmip_response.json()['value']['full_name']['default_message']
                   else:
                       vm['ip_address'] = "IP not assigned/VMware tools not installed"
                       vm['os'] = "IP not assigned/VMware tools not installed"

                   vm_mac_details = []
                   for nic in vm_mac_response.json()['value']['nics']:
                       vm_mac_details.append(nic['value']['mac_address'].strip('\''))
                       vm['mac'] = vm_mac_details
                   vm_details.append(vm)
               else:
                   logging.error("No vms mapped to resource pool : {0}".format(rsPool))
           return vm_details
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting VM details : ' + str(e))

   def get_session_id(self, vcip, vc_User, vc_Password):
       '''
       API call being made to get the session_id w
       :param vcip:
       :param vc_User:
       :param vc_Password:
       :return: vc_session_id
       '''
       logging.debug('Getting the VCenter session_id')
       try:
           url = 'https://{0}/rest/com/vmware/cis/session'.format(vcip)
           response = requests.post(url,auth=(vc_User, vc_Password),verify=False)
           vc_session_id = response.json()['value']
           return vc_session_id
       except Exception as e:
           self.LogException.log_and_raise_exception('vCenter session-id generation failed : ' + str(e))

   def del_session_id(self,vcip,vc_session_id):
      logging.debug('Deleting VCenter api session')
      try:
          url = 'https://{0}/rest/com/vmware/cis/{1}'.format(vcip,vc_session_id)
      except Exception as e:
          self.LogException.log_and_raise_exception('vCenter session-id deletion failed : ' + str(e))

   def get_rsPool_id(self,vcip,rsPool,vc_session_id):
       logging.debug('Getting Resource Pool ID')
       rsPool_id = None
       url = 'https://{0}/rest/vcenter/resource-pool?filter.names.1={1}'.format(vcip,rsPool)
       response = requests.get(url, verify=False, headers={"vmware-api-session-id": vc_session_id})
       rsPool_id = response.json()['value'][0]['resource_pool']
       if not rsPool_id:
           self.LogException.log_and_raise_exception('No corresponding resource pool found')
       return rsPool_id
