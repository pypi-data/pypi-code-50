#!/usr/bin/env python3

import os
import hcl
import yaml
import paramiko
import logging
import requests
import subprocess
import configparser
from os import listdir
from datetime import datetime
from datetime import timedelta
from os.path import isfile, join
from subprocess import Popen, PIPE
from time import sleep
from . log_exception import LogException
from . import global_vars

class LoggingMonitoringDetails:
   LogException = LogException()
   def get_vault_service_details(self,inventory_dict, config_dict, ansible_dict,key_file):
       try:
           logging.debug('Getting Vault Service details')
           vault_service = {}
           if ((inventory_dict['vault_server'] is not None and len(inventory_dict['vault_server']) > 0)):
               vault_ip = inventory_dict['vault_server'][0]
               vault_service['name'] = 'Vault'
               vault_service['components'] = []
               ssh_client = self.get_ssh_client(vault_ip,key_file,ansible_dict['remote_user'])
               command = 'vault --version'
               (stdin, stdout, stderr) = ssh_client.exec_command(command,get_pty=True)
               exit_status = stdout.channel.recv_exit_status()
               logging.debug("output for vault command : {0}".format(stdout))
               logging.debug("Error for vault command : {0}".format(stderr))
               vault_version = None
               for line in stdout.readlines():
                  if line.startswith('Vault'):
                     vault_version = line
                     break
               if vault_version is not None:
                   vault_service['components'].append(vault_version)
               ssh_client.close()
           else:
               logging.error('vault component not found in inventory')
           return vault_service
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting vault service details : ' + str(e))

   def get_logging_service_details(self,inventory_dict, config_dict, ansible_dict, ansible_vars_dict, key_file):
       try:
           logging.debug('Getting Logging Service details')
           logging_service = {}
           if ((inventory_dict['aggregator'] is not None and len(inventory_dict['aggregator']) > 0) or (inventory_dict['elasticsearch'] is not None and len(inventory_dict['elasticsearch']) > 0) or (inventory_dict['kibana'] is not None and len(inventory_dict['kibana']) > 0)):
               logging_service['name'] = 'Logging'
               logging_components = []
               is_single_node = True if config_dict['single_node'].strip('\"').lower() == 'yes' else False
               tdagent_version = self.get_tdagent_version(key_file, inventory_dict, ansible_dict)
               if tdagent_version is not None:
                   logging_components.append(tdagent_version)
            
               elasticsearch_version = self.get_elasticsearch_version(is_single_node, inventory_dict, ansible_vars_dict['elasticsearch_user'], ansible_vars_dict['elasticsearch_password'])
               if elasticsearch_version is not None:
                   logging_components.append(elasticsearch_version)

               kibana_version = self.get_kibana_version(is_single_node, key_file, inventory_dict, ansible_dict)
               if kibana_version is not None:
                   logging_components.append(kibana_version)

               logging_service['components'] = logging_components
               logging.debug('Logging Service details : {0}'.format(logging_service))
           else:
               logging.error('Logging components not found in inventory')
           return logging_service
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting logging service details : ' + str(e))
   def get_consul_version(self,inventory_dict, config_dict, ansible_dict, key_file):
       try:
           consul_ip = None
           consul_service = {}
           if(inventory_dict['consul_servers'] is not None and len(inventory_dict['consul_servers']) > 0):
               consul_ip = inventory_dict['consul_servers'][0]
               consul_service['name'] = 'Consul'
               consul_service['components'] = []
               command = 'consul version'
               if(consul_ip =='localhost'):
                  cmd=subprocess.Popen(['consul', 'version'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
                  (stdout, stderr) = cmd.communicate()
                  logging.debug("output for consul command : {0}".format(stdout))
                  logging.debug("Error for consul command : {0}".format(stderr))
                  consul_version=stdout.splitlines()[0].decode("utf-8")
                  consul_service['components'].append(consul_version)
               else:
                  ssh_client = self.get_ssh_client(consul_ip,key_file,ansible_dict['remote_user'])
                  (stdin, stdout, stderr) = ssh_client.exec_command(command,get_pty=True)
                  logging.debug("output for consul command : {0}".format(stdout))
                  logging.debug("Error for consul command : {0}".format(stderr))
                  consul_version = None
                  for line in stdout.readlines():
                
                      if line.startswith('Consul'):
                        consul_version = line
                        consul_service['components'].append(consul_version)
                        break
                  if consul_version is None:
                     logging.error("consul version not found in {0}".format(consul_ip))
                  ssh_client.close()
       
           else: 
               logging.error('consul ip not found in inventory')
           return consul_service
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting consul service details : ' + str(e))

   def get_tdagent_version(self,key_file, inventory_dict, ansible_dict):
       if (inventory_dict['aggregator'] is not None and len(inventory_dict['aggregator']) > 0):
           aggregator_ip = inventory_dict['aggregator'][0]
           ssh_client = self.get_ssh_client(aggregator_ip, key_file,ansible_dict['remote_user'] )
           command = 'rpm -q td-agent'
           (stdin, stdout, stderr) = ssh_client.exec_command(command)
           logging.debug("output for td-agent command : {0}".format(stdout))
           logging.debug("Error for td-agent command : {0}".format(stderr))
           tdagent_version = None
           for line in stdout.readlines():
               if line.startswith('td-agent'):
                   tdagent_version =  line
                   break
           if tdagent_version is None:
               logging.error("td-agent version not found in {0}".format(aggregator_ip))
           ssh_client.close()
           return tdagent_version
       else:
           logging.error('aggregator group not found in inventory')

   def get_elasticsearch_version(self,is_single_node, inventory_dict, elastic_user, elastic_password):
       elasticsearch_ip = None
       if(is_single_node is True and inventory_dict['aggregator'] is not None and len(inventory_dict['aggregator']) > 0):
           elasticsearch_ip = inventory_dict['aggregator'][0]
       elif(is_single_node is False and inventory_dict['elasticsearch'] is not None and len(inventory_dict['elasticsearch']) > 0):
           elasticsearch_ip = inventory_dict['elasticsearch'][0]
       else:
           logging.error('elastic search ip not found in inventory')
           return

       response = requests.get('https://{0}:9200'.format(elasticsearch_ip),verify=False,auth=(elastic_user, elastic_password))
       response.raise_for_status()
       elastic_details = response.json()
       if 'version' in elastic_details:
           return 'elasticsearch-{0}'.format(elastic_details['version']['number'])
       else:
           logging.error("elasticsearch version not found in {0}".format(elasticsearch_ip))

   def get_kibana_version(self, is_single_node, key_file, inventory_dict, ansible_dict):
       kibana_ip = None
       if(is_single_node is True and inventory_dict['aggregator'] is not None and len(inventory_dict['aggregator']) > 0):
           kibana_ip = inventory_dict['aggregator'][0]
       elif(is_single_node is False and inventory_dict['kibana'] is not None and len(inventory_dict['kibana']) > 0):
           kibana_ip = inventory_dict['kibana'][0]
       else:
           logging.error('kibana ip not found in inventory')
       ssh_client = self.get_ssh_client(kibana_ip, key_file,ansible_dict['remote_user'])
       command = 'rpm -q kibana'
       (stdin, stdout, stderr) = ssh_client.exec_command(command)
       logging.debug("output for kibana command : {0}".format(stdout))
       logging.debug("Error for kibana command : {0}".format(stderr))
       kibana_version = None
       for line in stdout.readlines():
           if line.startswith('kibana'):
               kibana_version = line
               break
       if kibana_version is None:
           logging.error("kibana version not found in {0}".format(kibana_ip))
       ssh_client.close()
       return kibana_version

   def get_ssh_client(self, ip_address, key_file, host_user):
       try:
           logging.debug('Getting SSH connection to {0}'.format(ip_address))
           ssh_client = paramiko.SSHClient()
           ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
           ssh_client.connect(ip_address, port=22, username=host_user, key_filename=key_file)
           logging.debug('Got SSH connection to {0}'.format(ip_address))
           return ssh_client
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting ssh client : ' + str(e))

   def get_deployment_time_for_logging(self, config_dict):
       latest_log_file =self.get_latest_logging_deployment_logfile()
       if latest_log_file is not None  and len(latest_log_file) > 0:
           deployment_time = self.find_logging_deployment_time_from_log(os.path.join(global_vars.IAC_LOG_PATH, latest_log_file),config_dict)['execution_time']
           start_time = (self.find_logging_deployment_time_from_log(os.path.join(global_vars.IAC_LOG_PATH, latest_log_file),config_dict)['start_time']).strip()
           if(deployment_time == None):
               now = datetime.now()
               current_time = now.strftime("%H:%M:%S")
               fmt='%H:%M:%S'
               diff = datetime.strptime(current_time,fmt)-datetime.strptime(start_time,fmt)
               deployment_time = self.format_time(diff.seconds)        
           return deployment_time

   def get_latest_logging_deployment_logfile(self):
       try:
           logging.debug('Getting the latest logging deployment log from {0}'.format(global_vars.IAC_LOG_PATH))
           latest_log_file_name = ''
           if os.path.exists(global_vars.IAC_LOG_PATH):
               log_files = [f for f in listdir(global_vars.IAC_LOG_PATH) if isfile(join(global_vars.IAC_LOG_PATH, f))]
               datemask = "%Y-%m-%d_%H:%M:%S"
               for logfile in log_files:
                   if(logfile.startswith(global_vars.IAC_LOG_FILE_NAME_PREFIX)):
                       if(latest_log_file_name == ''):
                           latest_log_file_name = logfile
                           continue       
                       logfile_time_str = logfile.split("_",2)[2].strip('.log')                   
                       logfile_time_dt = datetime.strptime(logfile_time_str, datemask)
                       latest_logfile_time_str = latest_log_file_name.split("_",2)[2].strip('.log')
                       latest_logfile_time_dt = datetime.strptime(latest_logfile_time_str, datemask)
                       if(logfile_time_dt > latest_logfile_time_dt):
                           latest_log_file_name = logfile
               if latest_log_file_name == '':
                   logging.error("IaC Deployment log file with prefix {0} not found".format(global_vars.IAC_LOG_FILE_NAME_PREFIX))
               logging.debug('Latest IaC deployment log file {0}'.format(latest_log_file_name))
               return latest_log_file_name
           else:
               logging.error("IaC Logs directory {0} not found".format(global_vars.IAC_LOG_PATH))
       except Exception as e:
           self.LogException.log_and_raise_exception('Exception occurred while getting latest IaC deployment log : ' + str(e))

   def find_logging_deployment_time_from_log(self,log_file,config_dict):
       logging.debug('Finding logging deployment time')
       start_time = None
       execution_time = None
       with open(log_file, 'r') as f:
           while True:
               line = f.readline()
               if ('Execution started' in line):
                  start_time_line = line
                  start_line_array = start_time_line.split(' ')
                  start_time = start_line_array[len(start_line_array) - 1]
               if line == '':
                   break

               if (global_vars.IAC_SUCCESS_MESSAGE) in line:
                   execution_time_line = f.readline()
                   line_array = execution_time_line.split(':')
                   execution_time = line_array[len(line_array) - 1]

           return {'start_time':start_time,'execution_time':execution_time}
       logging.error("Successful Deployment Time for IaC could not be found")

   def format_time(self,seconds):
       hours=str(seconds//3600)
       mins=str((seconds%3600)//60)
       sec=str((seconds%3600)%60)[:2]
       time_formatted = "{}hr {}mins {}sec".format(hours, mins,sec)
       return time_formatted
