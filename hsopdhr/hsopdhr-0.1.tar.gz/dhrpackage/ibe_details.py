#!/usr/bin/env python3

import os
import yaml
import paramiko
import logging
import requests
from . log_exception import LogException

class IbeDetails: 
   LogException = LogException()
   def get_ibe_details(self,inventory_dict):
       try:
           logging.debug('Getting IBE Service details')
           ibe_service = {}
           if inventory_dict['ibe'] is not None and len(inventory_dict['ibe']) > 0:
               ibe_ip = inventory_dict['ibe'][0]
               response = requests.get('http://{0}:4444/IBE/discovery'.format(ibe_ip))
               response.raise_for_status()
               ibe_details = response.json()
               ibe_service['name'] = 'IBE'
               ibe_service['components'] = []
               if 'productversion' in ibe_details:
                   productid = ibe_details['productid']
                   productversion = ibe_details['productversion']
                   ibe_service['components'].append(productid + '-' + productversion)
               logging.debug('IBE Service details : {0}'.format(ibe_service))
           else:
               logging.error('ibe group not found in inventory')
           
           return ibe_service
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting IBE service details Details : {0}'.format(str(e)))           