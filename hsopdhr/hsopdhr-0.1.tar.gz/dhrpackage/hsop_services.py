#!/usr/bin/env python3

import os
import yaml
import paramiko
import logging
import requests
from . logging_monitoring_details import LoggingMonitoringDetails
from . ibe_details import IbeDetails
from . log_exception import LogException
from datetime import datetime

class HsopServices:
   LoggingMonitoringDetails = LoggingMonitoringDetails()
   IbeDetails = IbeDetails()
   LogException = LogException()
   def get_service_details(self, config_dict, inventory_dict, ansible_dict, ansible_vars_dict,hsop_repoPath):
       logging.debug('Getting Core services details')
       try:           
           key_file = hsop_repoPath+"/ansible/"+ansible_dict['private_key_file'].strip("../")            
           service_details = []
           consul_details = self.LoggingMonitoringDetails.get_consul_version(inventory_dict, config_dict, ansible_dict,key_file)
           if len(consul_details) > 0:
               service_details.append(consul_details)
           vault_details = self.LoggingMonitoringDetails.get_vault_service_details(inventory_dict, config_dict, ansible_dict, key_file)
           if len(vault_details) > 0:
               service_details.append(vault_details)
           logging_details = self.LoggingMonitoringDetails.get_logging_service_details(inventory_dict, config_dict, ansible_dict, ansible_vars_dict, key_file)
           if len(logging_details) > 0:
               service_details.append(logging_details)
           ibe_details = self.IbeDetails.get_ibe_details(inventory_dict)
           if len(ibe_details) > 0:
               service_details.append(ibe_details)
           return service_details
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting Core service details Details : {0}'.format(str(e)))