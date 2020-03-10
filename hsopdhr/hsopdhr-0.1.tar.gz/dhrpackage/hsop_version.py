#!/usr/bin/env python3

import os
import yaml
import paramiko
import logging
import requests
from . log_exception import LogException
class HsopVersion:
   LogException = LogException()
   def get_hsop_version(self,inventory_dict,config_dict,BUILD_CONF):
       try:
           hsop_version = None
           logging.debug('Getting HSOP version details')
           with open(BUILD_CONF, 'r') as file:
               line = file.readline()
               if line.startswith(('HSoP','hsop','HSOP')):
                   hsop_version = line
               else:
                   logging.error('HSOP version not captured in : {0}'.format(BUILD_CONF_FILE))
           return hsop_version

       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while checking for build_version.conf file :{0}'.format(str(e)))           
