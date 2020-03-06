import requests
import numpy as np
import base64
import jwt
import pandas as pd
import pickle
import os
import getpass
from functools import reduce
import uuid
import json
import ntpath
from pandas.io.json import json_normalize

class RapidMinerGoClient():

    def __init__(self, server, username,password= ""):
        # variables
        self.httpHeader = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        self.SERVER = server
        self.USERNAME = username


        if(not password):
            # RapidMiner Server Password
            print("password not found")
            self.password = getpass.getpass(prompt='Please enter your Password: ')
        else:
            print("password found")
            self.password = password

        # connect
        self.__connect()

        # set last variables
        self.__last_data_id = ''
        self.__last_data_ = {}
        self.__last_mod_task = {}
        self.__last_mod_task_id = ''
        self.__last_execution = ''
        self.__last_result = {}
        self.__last_models = []
        self.__bestModel = ''
        self.__maxGain = 0.0


    def __connect(self):
        # Encode the basic Authorization header
        # userAndPass = base64.b64encode(bytes(self.USERNAME + ":" + self.password, 'utf-8')).decode("ascii")
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json'}

        body = {
            'username': self.USERNAME,
            'password': self.password
        }

        r = requests.post(url=self.SERVER + '/rmid/api/login', data=json.dumps(body), headers=headers)
        # JWT idToken for the RM Server
        self.idToken = r.json()['token']
        # Bearer Authorization header
        self.auth_header = {
            'Accept': 'application/json',
            'Cookie': 'token=%s' % self.idToken
        }

        self.cookieToken = {
            'token': self.idToken
        }

        # RM Server Client Info
        if (r.status_code == 200):
            print("Successfully connected to the Server")
        else:
            print("Connection Error")

    def add_data_file(self, filepath):
        # check if filepath exists and that is not a directory
        if (ntpath.exists(filepath)) & (ntpath.split(filepath)[-1] != ''):
            print("File exists")
            filename = ntpath.split(filepath)[-1]
            file = filepath
        else:
            return print("File not found, please check the filepath")

        # check that the file is correct format

        payload = {
            'name': 'file',
            'filename': filename
        }

        files = {
            'file': open(file, 'rb')
        }

        r = requests.post(self.SERVER + '/am/api/data',
                          cookies=self.cookieToken,
                          data=payload,
                          files=files,
                          allow_redirects=False)

        if (r.status_code == 200):
            print("Successfully uploaded data")
            print("Please remember the following file ID")
            print(r.json()['id'])
            self.__last_data_id = r.json()['id']
            self.__last_data_ = r.json()

        return r.json()

    def add_dataFrame(self, df):
        # make a new folder
        if not os.path.exists('/tmp001'):
            os.mkdir('/tmp001')
        # save as csv
        df.to_csv('/tmp001/0001.csv', index=False)

        payload = {
            'name': 'file',
            'filename': '0001.csv'
        }

        files = {
            'file': open('/tmp001/0001.csv', 'rb')
        }

        r = requests.post(self.SERVER + '/am/api/data',
                          cookies=self.cookieToken,
                          data=payload,
                          files=files,
                          allow_redirects=False)

        if (r.status_code == 200):
            print("Successfully uploaded data")
            print("Please remember the following file ID")
            print(r.json()['id'])
            self.__last_data_id = r.json()['id']
            self.__last_data_ = r.json()
            # os.remove('/tmp001/0001.csv')
            # os.rmdir('/tmp001')

        return r.json()

    def get_data_info(self, dataId):
        # create data request URL
        url = self.SERVER + '/am/api/data/' + dataId

        r = requests.get(
            url,
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            print("Successfully got data info")
            return r.json()
        else:
            # improve
            print("ERROR, data not found")

    def create_modeling_task(self, dataId):
        request = {
            "dataId": dataId,
            "type": "new"
        }
        url = self.SERVER + '/am/api/modelingtasks'

        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            print("Successfully created modeling task")
            self.__last_mod_task_id = r.json()['id']
            self.__last_mod_task = r.json()
            return r.json()
        else:
            # improve
            print("ERROR, data not found")

    def get_modeling_task(self, modTaskId):
        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId

        r = requests.get(
            url,
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            # print('\n\nGot Modeling Task:\n', json.dumps(r.json(), indent=4, sort_keys=True))
            return r.json()
        else:
            print("EROR: Non existing modelling task")

    def set_label(self, modTaskId, labelAtt):
        request = {
            "attributeName": labelAtt
        }

        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId + '/label'

        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            print("Successfully set Target Label!")
            #print(r.json())
            self.__last_mod_task = self.get_modeling_task(modTaskId)
            self.__last_mod_task_id = self.__last_mod_task['id']
            #print(r.json()['displayName'])
            #print(r.json()['label']['classOfHighestInterest'])
        else:
            print("Error. Modeling Task not found")

    def set_class_interest(self, modTaskId, highvalue_class, low_value_class):
        request = {
            "highestValue": highvalue_class,
            "lowestValue": low_value_class
        }

        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId + '/label/classinterest'

        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )
        if r.status_code == 200:
            print("Success set class of interest!")
            #print(r.json())
            self.__last_mod_task = self.get_modeling_task(modTaskId)
            self.__last_mod_task_id = self.__last_mod_task['id']
            # self.__last_mod_task = r.json()
            # print(r.json()['displayName'])
            # print(r.json()['label']['classOfHighestInterest'])
        else:
            print("Error. Modeling Task not found")

    def set_cost_matrix(self, modTaskId, costMatrix=[["1", "-1"], ["-1", "1"]]):
        request = {
            "costMatrixData": costMatrix
        }
        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId + '/costmatrix'
        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )
        if r.status_code == 200:
            print("Success! Cost Matrix updated")
            self.__last_mod_task = self.get_modeling_task(modTaskId)
            self.__last_mod_task_id = self.__last_mod_task['id']
            #print(json.dumps(self.__last_mod_task, indent=4, sort_keys=True))
            # self.__last_mod_task = r.json()
            # print(r.json()['costMatrixDTO']['costMatrixData'])
        else:
            print("Error. Cost Matrix Couldn't be updated")
        return self.__last_mod_task

    def set_preprocessing(self, modTaskId, correlationBetweenColumns=False, explainPredictions=False,
                          importanceOfColumns=True,
                          extractDates=False, extractTexts=False, maximumNumberOfValues=50,
                          numberOfExtractedFeatures=100, removeColumnsWithTooManyValues=True, selectedTextColumns=[],
                          accurrancyBalance="ACCURATE", additionalMinutes=60, automaticFeatureGeneration=False,
                          automaticFeatureSelection=False, functionComplexity="MEDIUM"):
        request = {
            "columnConfig": {
                "correlationBetweenColumns": correlationBetweenColumns,
                "explainPredictions": explainPredictions,
                "importanceOfColumns": importanceOfColumns
            },
            "dataPrepConfig": {
                "extractDates": extractDates,
                "extractTexts": extractTexts,
                "maximumNumberOfValues": maximumNumberOfValues,
                "numberOfExtractedFeatures": numberOfExtractedFeatures,
                "removeColumnsWithTooManyValues": removeColumnsWithTooManyValues,
                "selectedTextColumns": selectedTextColumns
            },
            "featureEngineeringConfig": {
                "accurrancyBalance": accurrancyBalance,
                "additionalMinutes": additionalMinutes,
                "automaticFeatureGeneration": automaticFeatureGeneration,
                "automaticFeatureSelection": automaticFeatureSelection,
                "functionComplexity": functionComplexity
            }
        }

        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId + '/preprocessing'

        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            print("Success! Preprocessing updated")
            print('\n\nSet preprocessing response:\n', json.dumps(r.json(), indent=4, sort_keys=True))
            self.__last_mod_task = self.get_modeling_task(modTaskId)
            self.__last_mod_task_id = self.__last_mod_task['id']

        else:
            print("Error. Preprocessing Couldn't be updated")

    def set_model_inputs(self, modTaskId, variableList):

        namelist = []
        for i in range(len(self.__last_mod_task['modelInputs'])):
            namelist.append(self.__last_mod_task['modelInputs'][i]['attributeName'])

        request = []
        for varname in variableList:
            if varname in namelist:
                request.append({"attributeName": varname})
            else:
                print("Variable: " + varname + " is not on the dataset")

        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId + '/modelinputs'

        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            print("Success! Variables updated")
            self.__last_mod_task = self.get_modeling_task(modTaskId)
            self.__last_mod_task_id = self.__last_mod_task['id']
            print(json.dumps(r.json(), indent=4, sort_keys=True))
        else:
            print("Error. Model inputs Couldn't be updated")

    def update_models(self, modTaskId, to_disable):
        url = self.SERVER + '/am/api/modelingtasks/' + modTaskId + '/models'
        for model in to_disable:
            request = {
                "type": model,
                "selected": False
            }
            r = requests.post(
                url, json.dumps(request),
                headers=self.httpHeader,
                cookies=self.cookieToken,
                allow_redirects=False
            )

            print('Disabled model:', model, json.dumps(response, indent=4, sort_keys=True))

    def start_execution(self, modTaskId):
        request = {
            "type": "modelingTask",
            "modelingTaskId": modTaskId
        }
        url = self.SERVER + '/am/api/executions'

        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken
        )
        if r.status_code == 200:
            self.__last_execution = r.json()
            #print('\n\nStarted execution:\n', json.dumps(r.json(), indent=4, sort_keys=True))

        else:
            print("EXECUTION ERROR")

    def get_modeling_execution(self, modTaskId):
        url = self.SERVER + '/am/api/executions'
        params = {
            'mti': modTaskId
        }
        r = requests.get(
            url,
            params=params,
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )

        if r.status_code == 200:
            self.__last_execution = r.json()
            #print('\n\nGot Modeling Task Execution:\n', json.dumps(r.json(), indent=4, sort_keys=True))

        else:
            print("ERROR retrieving modeling task status")

        return r.json()

    def get_execution_result(self, modTaskId):
        url = self.SERVER + '/am/api/executions/result'
        allResults = {}
        model_types = map(lambda x: x['type'], self.__last_execution)
        for model in model_types:
            params = {
                'mti': modTaskId,
                'model': model
            }
            r = requests.get(
                url,
                headers=self.httpHeader,
                cookies=self.cookieToken,
                params=params,
                allow_redirects=False
            )
            #print('Got execution response for: ', model)
            #allResults.append(r.json())

            print('Got execution result for  ', model)
            #print('Response is: ', r.json())
            result = {}
            result[model] = r.json()
            allResults.update(result)
        self.__last_result = allResults
        self.__last_models = model_types
        return allResults

    #This function finds the best model and deploys the best model
    #params: list, list of features to get the required value
    #return: bestModel
    def determine_best_model(self, features):
        print('Inside determine_best_model function')
        model_types = map(lambda x: x['type'], self.__last_execution)
        for model in model_types:
                print("check model : "+model)
                resultForModel = self.__last_result[model]
                for feature in features :
                    if resultForModel:
                        resultForModel = self.getValuesOutOfList(feature, resultForModel)
                print(len(resultForModel))
                if len(resultForModel)>0  and str(resultForModel) != '' :
                    resultForModel = resultForModel.split(' ')[0].replace('%', '');
                    print(resultForModel)
                    print(float(resultForModel)>float(self.__maxGain))
                    if (float(resultForModel)>float(self.__maxGain)):
                        #print('Change in best model')
                        #print(resultForModel)
                        #print(model)
                        self.__maxGain = resultForModel
                        self.__bestModel = model
        print('Exiting determine_best_model function with BestModel:'+str(self.__bestModel)+' param:'+str(self.__maxGain))
        return self.__bestModel

    #This function gets the value out of the dictionary
    #params: string, dictionary
    #return: dictionary
    def getValuesOutOfList(self, feature, resultForModel):
        if feature in resultForModel.keys():
            resultForModel = resultForModel[feature]
        else :
            print('Wrong feature:'+ feature+ ' not available in the result')
            resultForModel = []
        return resultForModel

    def resultPerformancePercentageView(self, features):
        #print('Inside determine_best_model function')
        jsonList=[]
        listmodels = []
        model_types = map(lambda x: x['type'], self.__last_execution)
        for model in model_types:
            if model != 'WEIGHTS':
                listmodels.append(str(model))
                print("check:" + model)
                resultForModel = self.__last_result[model]
                for feature in features:
                    if resultForModel:
                        resultForModel = self.getValuesOutOfList(feature, resultForModel)
                for eachResult in resultForModel:
                    val = resultForModel[eachResult]
                    resultForModel[eachResult] = val.split(' ')[0]
                jsonList.append(resultForModel)
        #print(jsonList)
        result = json_normalize(jsonList)
        result['Model'] = listmodels
        return result

    def deploy_model(self, modTaskId, selected_model):
        request = {
            "modelingTaskId": modTaskId,
            "modelType": selected_model
        }
        url = self.SERVER + '/am/api/deployments'
        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )
        print('\n\nDeployed', selected_model, ':\n', json.dumps(r.json(), indent=4, sort_keys=True))
        deploymentId = r.json()['id']
        return deploymentId

    def score(self, data, deploymentId):
        request = {
            "data": data
        }
        url = self.SERVER + '/am/api/deployments/' + deploymentId
        r = requests.post(
            url, json.dumps(request),
            headers=self.httpHeader,
            cookies=self.cookieToken,
            allow_redirects=False
        )
        #print('\n\nScore results:\n', json.dumps(r.json(), indent=4, sort_keys=True))

        return r.json()

    def quick_automodel(self,training_data,label):
        response_json = self.add_dataFrame(training_data)
        data_id = response_json["id"]
        print(data_id)
        modeling_task = self.create_modeling_task(data_id)
        print(modeling_task)
        modeling_task_id = modeling_task["id"]
        self.set_label(modeling_task_id, "Survived")
        self.set_class_interest(modeling_task_id, 'Yes', 'No')
        self.set_cost_matrix(modeling_task_id, [[1, -1], [-1, 1]])
        self.start_execution(modeling_task_id)
        self.get_modeling_execution(modeling_task_id)
        result = self.get_execution_result(modeling_task_id)


    # def quick_autoModel(self, dataframe, label):
        # print("Starting modeling process")
        # print("...")
        # print("Uploading data")
        # self.add_dataFrame(dataframe)
        # print("Data uploaded")
        # print("...")
        # print("Creating modelling task")
        # self.create_modeling_task(self.__last_data_id)
        # self.set_label(self.__last_mod_task_id, label)
        # print("Submitting modeling job")
        # self.start_execution(self.__last_mod_task_id)
        # print(
        #     "It might take a while to complete model training, you can check training status with the get_modeling_execution method and the modeling id below")
        # print(self.__last_mod_task_id)
        # os.remove('/tmp001/0001.csv')
        # os.rmdir('/tmp001')


'''
class RapidMinerClient():
    """docstring for RapidMinerClient"""
    def __init__(self,url,username):
    # URL of the Rapidminer Server
        self.server_url=url
        # RapidMiner Server Username
        self.username=username
        # RapidMiner Server Password
        self.password= getpass.getpass(prompt='Password: ')

        # Connect to the RM Server
        self.__connect()

        self.__package_path=os.path.dirname(os.path.abspath(__file__))

    # helper method to save process in the RapidMiner Repo(private)
    def __installRapidMinerProcess(self,fileName):
        file=open(self.__package_path+'\\'+fileName+'.xml')
        process=file.read()
        x=self.postProcess('/Python/process/'+fileName,process)
        file.close()
        # print(x.status_code)

    def __installRapidMinerServices(self,fileName):
        file=open(self.__package_path+'\\'+fileName+'.xml')
        descriptor=file.read()
        x=self.postService(fileName[:-10],descriptor)
        file.close()

    # helper method(private)
    def __connect(self):
        # Encode the basic Authorization header
        userAndPass = base64.b64encode(bytes(self.username+":"+self.password, 'utf-8')).decode("ascii")
        headers = { 'Authorization' : 'Basic %s' %  userAndPass }

        r=requests.get(url=self.server_url+'/internal/jaxrest/tokenservice',headers=headers)

        # JWT idToken for the RM Server
        self.idToken=r.json()['idToken']

        # Bearer Authorization header
        self.auth_header = { 'Authorization' : 'Bearer %s' %  self.idToken }

        # RM Server Client Info
        self.tokenDecoded=jwt.decode(r.json()['idToken'],verify=False)
        if(r.status_code==200):
            print("Successfully connected to the Server")
        else:
            print("Connection Error")

    def __dataFrameToExampleSet(self,data):
        attributes=list(data.columns)

        def createDict(row):
            mydict={}
            for i,key in enumerate(attributes):
                mydict[key]=str(row[i])
            return mydict

        exampleSet=list(map(lambda row: createDict(row) ,data.values))
        return exampleSet

    def installPackage(self):

        # install process on the server repo
        for filename in os.listdir(self.__package_path):
            if not filename.endswith('.xml'): continue

            if 'Descriptor' not in filename:
                self.__installRapidMinerProcess(filename[:-4])
            else:
                self.__installRapidMinerServices(filename[:-4])

    # path - path to the process/dataset on the repository
    # type - type of the fetch i.e through a process or dataset  
    def getData(self,path,dataType):
        if(dataType=="process"):
            numeric=1
        elif dataType== "data":
            numeric=2
        try:
            r=requests.post(self.server_url+"/api/rest/process/pythonGetData?",json={"path":path,"type":numeric},headers=self.auth_header)
            response=r.json()
            if(dataType=='process'):
                datasets=[pd.DataFrame(np.array([list(row.values()) for row in dataset]),columns=list(dataset[0].keys())) for dataset in response]
            else:
                datasets=pd.DataFrame(np.array([list(row.values()) for row in response]),columns=list(response[0].keys()))
            return datasets
        except Exception as e:
            print("Connection lost, reconnect to the Server ",e)

    def saveData(self,data,path):
        params=[{'key':'path','value':path},{'key':'sample','value':'15'}]
        response=self.submitService('pythonSaveData',data,params)
        # print(response.json())
        if response.status_code==200:
            print('Data saved Successfully')
        else:
            print('Error while saving data')

    # jobId= The jobId for a particular job
    def getJobs(self,jobId=None):
        if jobId==None:
            URL=self.server_url+"/executions/jobs"
        else:
            URL=self.server_url+"/executions/jobs/"+jobId
        # print(URL)
        r=requests.get(URL,headers=self.auth_header)
        # print(r.status_code)
        # response=r.json()

        # returns a JSON object tha has details for the particular job id or an array of Jobs with details under the content tag
        # return response

        return r

    def getQueues(self):
        URL=self.server_url+"/executions/queues?"
        print(URL)
        r=requests.get(URL,headers=self.auth_header)
        print(r.status_code)
        # response=r.json()

        # returns a JSON array of objects representing each queue withs it's properties
        # return response

        return r

    # method for getting the process XML
    def getProcessXML(self,path):
        URL=self.server_url+"/api/rest/resources"+path
        # print(URL)
        r=requests.get(URL,headers=self.auth_header)
        # print(r.status_code)
        # response=r.json()

        # returns the process XML as a string
        return r.text


    # method to submit job with raw XML
    # queueName - The name of the queue the process should be run on
    # processPath - The path of the process on the server to be encoded into base64 format
    # location - The location of the process
    def submitJobXML(self,queueName,process,location):

        URL=self.server_url+"/executions/jobs?"

        # convert process XML file to a string
        # processXML=et.parse(processPath)
        # process=et.tostring(processXML.getroot(),encoding='utf8',method='xml').decode('ascii')

        body={"queueName":queueName,"process":base64.b64encode(bytes(process,'utf-8')).decode("ascii"),"location":location}
        r=requests.post(url=URL,json=body,headers=self.auth_header)
        # print(r.status_code)
        return r

    #   method to submit job with with reference to process path on server
    def submitJob(self,queueName,processPath,params,location):
        processXML=self.getProcessXML(processPath)
        for param in params:
            processXML=processXML.replace(param['key'],param['value'])
        r=self.submitJobXML(queueName,processXML,location)
        return r

    #  method for submitting web services
    def submitService(self,serviceName,data=None,params=None):

        if data is None:
            body=[]
        else:
            body=self.__dataFrameToExampleSet(data)
        if params!=None:
            url=reduce(lambda final,param: final+param['key']+'='+param['value']+'&',params,'')
        else:
            url=''
        url=self.server_url+'/api/rest/process/'+serviceName+'?'+url
        r=requests.post(url=url,json=body,headers=self.auth_header)

        return r

    # method to save the process on the repo from the xml
    def postProcess(self,path,process):
        URL=self.server_url+"/api/rest/resources"+path
        # print(URL)
        head=self.auth_header.copy()
        head['Content-Type']='application/vnd.rapidminer.rmp+xml'
        r=requests.post(URL,headers=head,data=process)
        # print(r.status_code)
        # response=r.json()

        # returns the status message
        return r

    def postService(self,serviceName,descriptor):
        URL=self.server_url+"/api/rest/service/"+serviceName
        # print(URL)
        r=requests.post(URL,auth=(self.username,self.password),data=descriptor)
        # print(r.status_code)
        # response=r.json()

        # returns the status message
        return r

    def auto_model(self,data,label,models:list):

        self.guid=str(uuid.uuid4())
        self.saveData(data,'/Python/Data/'+self.guid+'/'+self.guid)
        params=[{'key':'%{guid}','value':self.guid},{'key': '%{label}', 'value': label}]
        response={}
        for model in models:
            r=self.submitJob('DEFAULT','/Python/process/'+model,params,'/Python/Data/'+self.guid+'/'+model+'/process')
            # print(r)
            response[model]=r.json()
        return response
'''