import inspect
import io
import logging
import requests
import time

from packaging import version

from .api_key import ApiKey
from .bucket_verification import BucketVerification
from .dataset import Dataset
from .dataset_instance import DatasetInstance
from .dataset_upload import DatasetUpload
from .deployment import Deployment
from .deployment_auth_token import DeploymentAuthToken
from .model import Model
from .model_instance import ModelInstance
from .organization import Organization
from .project import Project
from .project_dataset import ProjectDataset
from .project_dataset_schema import ProjectDatasetSchema
from .schema_validation import SchemaValidation
from .training_config_options import TrainingConfigOptions
from .use_case import UseCase
from .use_case_requirements import UseCaseRequirements
from .user import User
from .user_invite import UserInvite


class ApiException(Exception):
    def __init__(self, message, http_status, exception=None):
        self.message = message
        self.http_status = http_status
        self.exception = exception or 'ApiException'

    def __str__(self):
        return f'{self.exception}({self.http_status}): {self.message}'


class ReClient():
    client_version = '0.6.0'

    def __init__(self, api_key=None, server='https://realityengines.ai'):
        self.api_key = api_key
        self.server = server
        # Connection and version check
        try:
            documentation = self._call_api('documentation', 'GET')
            web_version = documentation['version']
            if version.parse(web_version) > version.parse(self.client_version):
                logging.info(
                    'A new version of the RealityEngines library is available')
                logging.info(
                    f'Current Version: {version} -> New Version: {web_version}')
            if api_key is not None:
                self.user = self._call_api('getUser', 'GET')
        except Exception:
            logging.error('Failed to connect to RealityEngines.AI server')
            raise

    def _call_api(
            self, action, method, query_params=None,
            body=None, files=None, parse_type=None):
        headers = {'apiKey': self.api_key,
                   'clientVersion': self.client_version, 'client': 'python'}
        url = self.server + '/api/v0/' + action

        response = self._request(
            url, method, query_params=query_params, headers=headers, body=body, files=files)
        result = None
        success = False
        error_message = None
        error_type = None
        try:
            json_data = response.json()
            success = json_data['success']
            error_message = json_data.get('error')
            error_type = json_data.get('errorType')
            result = json_data.get('result')
            if success and parse_type:
                if isinstance(result, list):
                    result = [parse_type(
                        self, **self._clean_values(r, parse_type)) for r in result if r is not None]
                else:
                    result = parse_type(
                        self, **self._clean_values(result, parse_type)) if result else None
        except Exception:
            error_message = response.text
        if not success:
            if response.status_code > 502 and response.status_code not in (501, 503):
                error_message = 'Internal Server Error, please contact dev@realityengines.ai for support'
            raise ApiException(error_message, response.status_code, error_type)
        return result

    def _clean_values(self, values, parse_type):
        type_inputs = inspect.signature(parse_type.__init__).parameters
        return {key: val for key, val in values.items() if key in type_inputs}

    def _request(self, url, method, query_params=None, headers=None,
                 body=None, files=None):
        if method == 'GET':
            return requests.get(url, params=query_params, headers=headers)
        elif method == 'POST':
            return requests.post(url, params=query_params, json=body, headers=headers, files=files, timeout=90)
        elif method == 'PUT':
            return requests.put(url, params=query_params, data=body, headers=headers, files=files, timeout=90)
        elif method == 'PATCH':
            return requests.patch(url, params=query_params, data=body, headers=headers, timeout=90)
        elif method == 'DELETE':
            return requests.delete(url, params=query_params, data=body, headers=headers)
        else:
            raise ValueError(
                'HTTP method must be `GET`, `POST`, `PATCH`, `PUT` or `DELETE`'
            )

    def _poll(self, obj, wait_states, delay=5, timeout=300):
        start_time = time.time()
        while obj.get_status() in wait_states:
            if timeout and time.time() - start_time > timeout:
                raise TimeoutError(f'Maximum wait time of {timeout}s exceeded')
            time.sleep(delay)
        return obj.describe()

    def add_organization_admin(self, user_id: str):
        '''Set a specific user as an admin for your organization. You can use the `List Organization Users API <https://realityengines.ai/app/help/ref/organization/listOrganizationUsers>`_ to see the userId for each user in your organization.    '''
        return self._call_api('addOrganizationAdmin', 'POST', body={'userId': user_id})

    def create_organization(self, name: str, workspace: str, discoverable: bool = 'True'):
        '''Create an organization with your company name and workspace you choose for the organization.    '''
        return self._call_api('createOrganization', 'POST', body={'name': name, 'workspace': workspace, 'discoverable': discoverable}, parse_type=Organization)

    def delete_invite(self, user_invite_id: str = None):
        '''Delete a User Invite. The invite associated with the specified email will be deleted from your organization and the link is no longer valid.    '''
        return self._call_api('deleteInvite', 'DELETE', query_params={'userInviteId': user_invite_id})

    def invite_user(self, email: str):
        '''Send an invite to a specified email.    '''
        return self._call_api('inviteUser', 'POST', body={'email': email}, parse_type=UserInvite)

    def join_organization(self, organization_id: str):
        '''Join an open organization. This API requires the organizationId you can find with the List Organizations API.    '''
        return self._call_api('joinOrganization', 'POST', body={'organizationId': organization_id})

    def list_organizations(self):
        '''List all public Organizations that match the domain of the current user's email address or that the current User has joined    '''
        return self._call_api('listOrganizations', 'GET', query_params={}, parse_type=Organization)

    def list_organization_users(self):
        '''List all of the users in your organization and the account information associated with each user.    '''
        return self._call_api('listOrganizationUsers', 'GET', query_params={}, parse_type=User)

    def list_user_invites(self):
        '''List all Invites sent to join the organization    '''
        return self._call_api('listUserInvites', 'GET', query_params={}, parse_type=UserInvite)

    def remove_user_from_organization(self, user_id: str):
        '''Remove a user from the organization.    '''
        return self._call_api('removeUserFromOrganization', 'DELETE', query_params={'userId': user_id})

    def delete_api_key(self, api_key_id: str):
        '''Delete a specified API Key.    '''
        return self._call_api('deleteApiKey', 'DELETE', query_params={'apiKeyId': api_key_id})

    def get_user(self):
        '''Get the current User's info    '''
        return self._call_api('getUser', 'GET', query_params={}, parse_type=User)

    def list_api_keys(self):
        '''List all of the API keys created by the current in the user's Organization    '''
        return self._call_api('listApiKeys', 'GET', query_params={}, parse_type=ApiKey)

    def add_project_dataset_column_type_override(self, project_id: str, dataset_id: str, column: str, column_type: str):
        '''    '''
        return self._call_api('addProjectDatasetColumnTypeOverride', 'POST', body={'projectId': project_id, 'datasetId': dataset_id, 'column': column, 'columnType': column_type}, parse_type=ProjectDatasetSchema)

    def create_project(self, name: str, use_case: str):
        '''Create a project with your specified project name and use case.    '''
        return self._call_api('createProject', 'GET', query_params={'name': name, 'useCase': use_case}, parse_type=Project)

    def delete_project(self, project_id: str):
        '''    '''
        return self._call_api('deleteProject', 'DELETE', query_params={'projectId': project_id})

    def describe_project(self, project_id: str):
        '''    '''
        return self._call_api('describeProject', 'GET', query_params={'projectId': project_id}, parse_type=Project)

    def describe_use_case_requirements(self, use_case: str):
        '''    '''
        return self._call_api('describeUseCaseRequirements', 'GET', query_params={'useCase': use_case}, parse_type=UseCaseRequirements)

    def get_project_dataset_schema(self, project_id: str, dataset_id: str):
        '''    '''
        return self._call_api('getProjectDatasetSchema', 'GET', query_params={'projectId': project_id, 'datasetId': dataset_id}, parse_type=ProjectDatasetSchema)

    def list_project_datasets(self, project_id: str):
        '''    '''
        return self._call_api('listProjectDatasets', 'GET', query_params={'projectId': project_id}, parse_type=ProjectDataset)

    def list_project_dataset_latest_instances(self, project_id: str):
        '''    '''
        return self._call_api('listProjectDatasetLatestInstances', 'GET', query_params={'projectId': project_id}, parse_type=DatasetInstance)

    def list_projects(self):
        '''    '''
        return self._call_api('listProjects', 'GET', query_params={}, parse_type=Project)

    def list_use_cases(self):
        '''    '''
        return self._call_api('listUseCases', 'GET', query_params={}, parse_type=UseCase)

    def remove_project_dataset_column_type_override(self, project_id: str, dataset_id: str, column: str):
        '''    '''
        return self._call_api('removeProjectDatasetColumnTypeOverride', 'DELETE', query_params={'projectId': project_id, 'datasetId': dataset_id, 'column': column}, parse_type=ProjectDatasetSchema)

    def set_project_dataset_column_types(self, project_id: str, dataset_id: str, column_overrides: dict):
        '''    '''
        return self._call_api('setProjectDatasetColumnTypes', 'POST', body={'projectId': project_id, 'datasetId': dataset_id, 'columnOverrides': column_overrides}, parse_type=ProjectDatasetSchema)

    def update_project(self, project_id: str, name: str):
        '''    '''
        return self._call_api('updateProject', 'PATCH', body={'projectId': project_id, 'name': name})

    def validate_project_datasets(self, project_id: str):
        '''    '''
        return self._call_api('validateProjectDatasets', 'GET', query_params={'projectId': project_id}, parse_type=SchemaValidation)

    def add_aws_role(self, bucket: str, role_arn: str):
        '''    '''
        return self._call_api('addAWSRole', 'POST', body={'bucket': bucket, 'roleArn': role_arn})

    def get_data_connector_verification(self, bucket: str):
        '''    '''
        return self._call_api('getDataConnectorVerification', 'GET', query_params={'bucket': bucket})

    def list_data_connector_verifications(self):
        '''    '''
        return self._call_api('listDataConnectorVerifications', 'GET', query_params={}, parse_type=BucketVerification)

    def remove_data_connector(self, bucket: str):
        '''    '''
        return self._call_api('removeDataConnector', 'DELETE', query_params={'bucket': bucket})

    def verify_data_connector(self, bucket: str):
        '''    '''
        return self._call_api('verifyDataConnector', 'POST', body={'bucket': bucket})

    def attach_dataset_to_project(self, dataset_id: str, project_id: str, project_dataset_type: str):
        '''Adds a dataset to an existing project    '''
        return self._call_api('attachDatasetToProject', 'POST', body={'datasetId': dataset_id, 'projectId': project_id, 'projectDatasetType': project_dataset_type}, parse_type=ProjectDataset)

    def delete_dataset(self, dataset_id: str):
        '''    '''
        return self._call_api('deleteDataset', 'DELETE', query_params={'datasetId': dataset_id})

    def describe_dataset(self, dataset_id: str):
        '''    '''
        return self._call_api('describeDataset', 'GET', query_params={'datasetId': dataset_id}, parse_type=Dataset)

    def read_dataset_from_cloud(self, name: str, location: str, file_format: str = None, project_id: str = None, project_dataset_type: str = None):
        '''    '''
        return self._call_api('readDatasetFromCloud', 'POST', body={'name': name, 'location': location, 'fileFormat': file_format, 'projectId': project_id, 'projectDatasetType': project_dataset_type}, parse_type=Dataset)

    def read_dataset_instance_from_cloud(self, dataset_id: str, location: str = None, file_format: str = None):
        '''    '''
        return self._call_api('readDatasetInstanceFromCloud', 'POST', body={'datasetId': dataset_id, 'location': location, 'fileFormat': file_format}, parse_type=DatasetInstance)

    def list_datasets(self):
        '''    '''
        return self._call_api('listDatasets', 'GET', query_params={}, parse_type=Dataset)

    def list_dataset_instances(self, dataset_id: str = None):
        '''    '''
        return self._call_api('listDatasetInstances', 'GET', query_params={'datasetId': dataset_id}, parse_type=DatasetInstance)

    def create_dataset_upload(self, name: str, file_format: str = None, project_id: str = None, project_dataset_type: str = None):
        '''    '''
        return self._call_api('createDatasetUpload', 'POST', body={'name': name, 'fileFormat': file_format, 'projectId': project_id, 'projectDatasetType': project_dataset_type}, parse_type=DatasetUpload)

    def create_dataset_instance_upload(self, dataset_id: str, file_format: str = None):
        '''    '''
        return self._call_api('createDatasetInstanceUpload', 'POST', body={'datasetId': dataset_id, 'fileFormat': file_format}, parse_type=DatasetUpload)

    def remove_dataset_from_project(self, dataset_id: str, project_id: str):
        '''    '''
        return self._call_api('removeDatasetFromProject', 'POST', body={'datasetId': dataset_id, 'projectId': project_id})

    def create_deployment(self, model_id: str, name: str, description: str = None, deployment_config: dict = None):
        '''    '''
        return self._call_api('createDeployment', 'POST', body={'modelId': model_id, 'name': name, 'description': description, 'deploymentConfig': deployment_config}, parse_type=Deployment)

    def create_deployment_token(self, project_id: str):
        '''    '''
        return self._call_api('createDeploymentToken', 'POST', body={'projectId': project_id}, parse_type=DeploymentAuthToken)

    def delete_deployment(self, deployment_id: str):
        '''    '''
        return self._call_api('deleteDeployment', 'DELETE', query_params={'deploymentId': deployment_id})

    def delete_deployment_token(self, auth_token: str = None):
        '''    '''
        return self._call_api('deleteDeploymentToken', 'DELETE', query_params={'authToken': auth_token})

    def describe_deployment(self, deployment_id: str):
        '''    '''
        return self._call_api('describeDeployment', 'GET', query_params={'deploymentId': deployment_id}, parse_type=Deployment)

    def list_deployments(self, project_id: str):
        '''    '''
        return self._call_api('listDeployments', 'GET', query_params={'projectId': project_id}, parse_type=Deployment)

    def list_deployment_tokens(self, project_id: str):
        '''    '''
        return self._call_api('listDeploymentTokens', 'GET', query_params={'projectId': project_id}, parse_type=DeploymentAuthToken)

    def start_deployment(self, deployment_id: str):
        '''    '''
        return self._call_api('startDeployment', 'GET', query_params={'deploymentId': deployment_id})

    def stop_deployment(self, deployment_id: str):
        '''    '''
        return self._call_api('stopDeployment', 'GET', query_params={'deploymentId': deployment_id})

    def update_deployment(self, deployment_id: str, name: str = None, description: str = None):
        '''    '''
        return self._call_api('updateDeployment', 'PATCH', body={'deploymentId': deployment_id, 'name': name, 'description': description})

    def complete_upload(self, dataset_upload_id: str):
        '''    '''
        return self._call_api('completeUpload', 'POST', body={'datasetUploadId': dataset_upload_id}, parse_type=Dataset)

    def describe_upload(self, dataset_upload_id: str):
        '''    '''
        return self._call_api('describeUpload', 'GET', query_params={'datasetUploadId': dataset_upload_id}, parse_type=DatasetUpload)

    def list_uploads(self):
        '''    '''
        return self._call_api('listUploads', 'GET', query_params={}, parse_type=DatasetUpload)

    def upload_file_part(self, dataset_upload_id: str, part_number: int, part_data: io.TextIOBase):
        '''    Upload a dataset part up to 5GB in size for a total file size of up to 5TB    '''
        return self._call_api('uploadFilePart', 'POST', query_params={'datasetUploadId': dataset_upload_id, 'partNumber': part_number}, files={'partData': part_data})

    def cancel_model_training(self, model_id: str):
        '''    '''
        return self._call_api('cancelModelTraining', 'DELETE', query_params={'modelId': model_id})

    def train_model(self, project_id: str, training_config: dict = None):
        '''    '''
        return self._call_api('trainModel', 'POST', body={'projectId': project_id, 'trainingConfig': training_config}, parse_type=Model)

    def delete_model(self, model_id: str):
        '''    '''
        return self._call_api('deleteModel', 'DELETE', query_params={'modelId': model_id})

    def describe_model(self, model_id: str):
        '''    '''
        return self._call_api('describeModel', 'GET', query_params={'modelId': model_id}, parse_type=Model)

    def get_model_metrics(self, model_id: str):
        '''    '''
        return self._call_api('getModelMetrics', 'GET', query_params={'modelId': model_id})

    def get_training_config_options(self, project_id: str):
        '''    '''
        return self._call_api('getTrainingConfigOptions', 'GET', query_params={'projectId': project_id}, parse_type=TrainingConfigOptions)

    def list_models(self, project_id: str):
        '''    '''
        return self._call_api('listModels', 'GET', query_params={'projectId': project_id}, parse_type=Model)

    def list_model_instances(self, model_id: str):
        '''    '''
        return self._call_api('listModelInstances', 'GET', query_params={'modelId': model_id}, parse_type=ModelInstance)

    def predict(self, auth_token: str, deployment_id: str, data: str, **kwargs):
        '''    '''
        return self._call_api('predict', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'data': data, **kwargs})

    def predict_lead(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('predictLead', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def predict_churn(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('predictChurn', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def predict_takeover(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('predictTakeover', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def predict_fraud(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('predictFraud', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def get_forecast(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('getForecast', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def get_recommendations(self, auth_token: str, deployment_id: str, query_data: str, num_items: int = '50', page: int = '1', include_filters: list = None, exclude_filters: list = None):
        '''    '''
        return self._call_api('getRecommendations', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data, 'numItems': num_items, 'page': page, 'includeFilters': include_filters, 'excludeFilters': exclude_filters})

    def get_ranked_items(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('getRankedItems', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def get_related_items(self, auth_token: str, deployment_id: str, query_data: str):
        '''    '''
        return self._call_api('getRelatedItems', 'POST', body={'authToken': auth_token, 'deploymentId': deployment_id, 'queryData': query_data})

    def batch_predict(self, deployment_id: str, input_location: str, output_location: str):
        '''    '''
        return self._call_api('batchPredict', 'POST', body={'deploymentId': deployment_id, 'inputLocation': input_location, 'outputLocation': output_location})
