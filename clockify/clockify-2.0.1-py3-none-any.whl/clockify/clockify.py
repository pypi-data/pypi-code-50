import requests
import json
import logging
logging.basicConfig(level=logging.INFO)

class Clockify():

    def __init__(self,api_key):

        self.base_url = 'https://api.clockify.me/api/' 
        self.api_key = api_key
        self.header =  {'X-Api-Key': self.api_key }

    def get_all_workspaces(self):
        try:
            url = self.base_url+'workspaces/'
            return self.__request_get(url)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
    
    def get_user (self, id):
        try:
            url = self.base_url + 'users/'+str(id)
            return self.__request_get(url)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    def get_all_projects (self, workspace_id):
        try:
            url = self.base_url+'workspaces/'+workspace_id+'/projects/'
            return self.__request_get(url)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    def get_all_workspace_users(self, workspace_id):
        try:
            url = self.base_url+'workspaces/'+workspace_id+'/users/'
            return self.__request_get(url)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
    
    def get_all_time_entry_user(self,workspace_id, user_id):
        try:
            url = self.base_url+'v1/workspaces/'+workspace_id+'/user/'+user_id+'/time-entries'
            r = self.__request_get(url)
            time_entries = []
            time_entries.append(r)
            has_time_entry = True
            page = 1
            
            while (has_time_entry):
                urlx = url + "/?page="+str(page)
                r = self.__request_get(urlx)
                if len(r) > 0:
                    time_entries.append(r)
                    page = page + 1
                elif len(r) < 50 or len(r) == 0:
                    has_time_entry = False
                    page = 1
                
            time_entries_list = []
            for time_entry in time_entries:
                for te in time_entry:
                    time_entries_list.append (te)
            
            return time_entries_list

        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
        
    def add_new_task(self, workspace_id, project_id, task_name, assigneeId = None):
        try:

            url = self.base_url+'workspaces/'+workspace_id+'/projects/'+project_id+'/tasks/'
            task = None
            if (assigneeId == None):
                task =  {'name': task_name, 'projectId': project_id }   
            else:
                task =  {'name': task_name, 'projectId': project_id, 'assigneeId': assigneeId}   
        
            return self.__request_post(url, task)

        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
    
    def __get_task(self, url):
        try:
            all_tasks = []
            next = True
            page = 0
            urlx = url
            while (next):
                tasks = self.__request_get(urlx)
                if len(tasks) == 0:
                    next = False
                for task in tasks:
                    if task in all_tasks:
                        next = False
                        break
                    all_tasks.append(task)
                page = page + 1  
                urlx = url + "?page="+str(page)
            return all_tasks
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    def get_task_done(self, workspace_id, project_id):
        try:
            url = self.base_url+'workspaces/'+workspace_id+'/projects/'+project_id+'/tasks/'
            return self.__get_task(url)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    def get_task_active (self, workspace_id, project_id):
        try:
            url = self.base_url+'workspaces/'+workspace_id+'/projects/'+project_id+'/tasks/?is-active=True'
            return self.__get_task(url)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
    
    def create_new_project(self, workspace_id, project_name):
        try:
            url = self.base_url+'workspaces/'+workspace_id+'/projects/'
            data = {
                    'name': project_name,
                    "clientId": "",
                    "isPublic": "false",
                    "estimate": {
                        "estimate": "3600",
                        "type": "AUTO" 
                        },
                    "color": "#f44336",
                    "billable": "false"
                }

            return self.__request_post(url, data)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    def create_new_workspace(self, name):
        try:
            url = self.base_url+'workspaces/'
            data = {'name': name}
            return self.__request_post(url, data)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
    
    def add_new_user(self,workspace_id, email):
        try:
            url = self.base_url+'workspaces/'+workspace_id+'/users'
            emails = []
            emails.append(email)
            data = {'emails': emails}
            return self.__request_post(url, data)
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    def __request_get(self,url):
        try:
            response = requests.get(url, headers=self.header)
            return response.json()
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)

    
    def __request_post(self,url,payload):
        try:
            response = requests.post(url, headers=self.header,json=payload)
            return response.json()
        except Exception as e:
            logging.error("Error: {0}".format(e))
            logging.error(e.__dict__)
