import json
from datetime import datetime
from typing import List, Optional
from urllib.parse import quote

import time
from isodate import duration_isoformat

from gateways.apis.api_route_base import ApiRoot
from gateways.common.cs18_api_classes import BlueprintRepositoryDetails, AccessLink
from gateways.common.cs18_api_converters import Converters
from gateways.common.cs18_api_errors import UnauthorizedException, MaxRetriesException, SandboxNotFound
from gateways.common.cs18_api_requests import (
    CreateInvitationsRequest,
    UpdateSpaceRequest,
    ProductionEnvironment, DebuggingServiceValue)
from gateways.common.cs18_api_responses import (AccountStatusResponse, BlueprintFileResponse, BlueprintResponse,
                                                CatalogForGetAllResponse, CatalogForGetResponse, CloudAccountResponse,
                                                CreateProductionResponse, CreateSandboxResponse, GetSpaceResponse,
                                                GetSpacesResponse, ProductionBlueResponse, ProductionGreenResponse,
                                                ProductionResponseLean, RepositoryResponse, RoleListItemResponse,
                                                SandboxResponse, SandboxResponseLean, TokenResponse,
                                                UserInvitationResponse, UserPermittedToSpaceResponse,
                                                UserForAllUsersResponse)
from gateways.n_session import NSession
from gateways.the_gateway import TheGateway
from gateways.utils import GatewayUtils, Utils


class Colony:
    # pylint: disable=too-many-public-methods
    def __init__(self, account: str, **kwargs):
        """
        :param account: account name
        :param Keyword Arguments:
            * access_token: either access token, or long token
            * email: account email
            * password: account password
            * host: address of Colony host machine, including port. Example: 'http://192.168.30.22:5050'
            * space: current space to be used
            * api_version: api version to be used
        """
        # raising an error when not provided valid credentials
        if (not kwargs.get("access_token")) and not (kwargs.get("email") and kwargs.get("password")):
            credentials = {
                "access_token": kwargs.get("access_token"),
                "email": kwargs.get("email"),
                "password": kwargs.get("password")
            }
            raise UnauthorizedException(credentials)

        gateway = TheGateway(provider=kwargs.get("provider"), host=kwargs.get("host"))
        self.session = NSession()
        self.api_address = GatewayUtils.get_cs18_api_address(
            provider=kwargs.get("provider"), host=kwargs.get("host")
        ).lower()

        self.refresh_token = \
            kwargs.get("access_token") if kwargs.get("access_token") else \
                gateway.account_login(
                    account=account,
                    email=kwargs.get("email"),
                    password=kwargs.get("password")
                ).refresh_token

        # use either provided access_token, or login with provided credentials
        self.access_token = \
            kwargs.get("access_token") if kwargs.get("access_token") else \
                gateway.account_login(
                    account=account,
                    email=kwargs.get("email"),
                    password=kwargs.get("password")
                ).access_token

        self.session.add_header(
            "Authorization",
            "Bearer {}".format(self.access_token)
        )
        self.space = kwargs.get("space", "Trial")
        self._api_version = kwargs.get("api_version")
        self._api_root = ApiRoot(
            api_address=self.api_address, space=self.space, version=self._api_version
        )


    def change_space(self, space: str):
        self.space = space
        self._api_root = ApiRoot(
            api_address=self.api_address, space=self.space, version=self._api_version
        )
        return self

    def get_spaces(self) -> List[GetSpacesResponse]:
        method_url = self._api_root.spaces.spaces()
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        spaces_json = json.loads(resp.text)
        return [Converters.create_spaces_response(space) for space in spaces_json]

    def get_account_status(self) -> AccountStatusResponse:
        method_url = self._api_root.settings.status()
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        return Converters.create_account_status_response(json.loads(resp.text))

    def get_about(self):
        method_url = self._api_root.about.api_about()
        resp = self.session.get(url=method_url)
        json_response = json.loads(resp.text)
        return json_response

    def get_cloud_accounts_under_account(self) -> List[CloudAccountResponse]:
        method_url = self._api_root.settings.cloud_accounts()
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        json_response = json.loads(resp.text)
        cloud_accounts = [
            Converters.create_cloud_account_response(x) for x in json_response
        ]
        return cloud_accounts

    def register_azure_account(self, with_tags: bool = False, **kwargs):
        """
        :param with_tags: bool
        :param kwargs:  name: str
                        subscription_id: str,
                        tenant_id: str,
                        application_id: str,
                        application_secret: str,
                        management_resource_group: str,
                        external_key: [str]
        """
        params = {"add_tags": with_tags}
        method_url = self._api_root.settings.azure_cloud_accounts()
        request = {
            "name": kwargs.get("name"),
            "subscription_id": kwargs.get("subscription_id"),
            "tenant_id": kwargs.get("tenant_id"),
            "application_id": kwargs.get("application_id"),
            "application_secret": kwargs.get("application_secret"),
            "management_resource_group": kwargs.get("management_resource_group"),
        }
        if kwargs.get("external_key"):
            request["id"] = kwargs.get("external_key")

        resp = self.session.post(url=method_url, json=request, params=params)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def register_aws_account(
            self,
            arn_role: str,
            external_id: str,
            name: str = None,
            external_key: str = None,
    ):
        """ Register AWS
        :param arn_role: IAM role ARN required for assume role to the customer cloud account
        :param external_id: External ID required for assume role to the customer cloud account
        :param name: Cloud account given name. If not passed its automatically generated by some pattern.
        :param external_key: Predefined external key that was already generated for another cloud account.
        May be used only for CI, tests and developers environments. Should not be used in production
        """
        method_url = self._api_root.settings.aws_cloud_accounts()
        request = {"arn_role": arn_role, "external_id": external_id}

        print("arn_role " + arn_role)

        if name:
            request["name"] = name
        if external_key:
            request["id"] = external_key

        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def add_azure_aks(self, name: str, cloud_account_name: str, kube_config: str):
        """ Register AKS"""
        method_url = self._api_root.settings.add_compute_service_aks()
        request = {
            "kube_config": kube_config,
            "name": name,
            "cloud_account_name": cloud_account_name,
        }

        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def add_aws_k8s_unmanaged(self, name: str, cloud_account_name: str, kube_config: str):
        method_url = self._api_root.settings.add_compute_service_aws_k8s_unmanaged()
        request = {
            "kube_config": kube_config,
            "name": name,
            "cloud_account_name": cloud_account_name,
        }

        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def update_aws_account(self, arn_role: str, external_id: str, name: str):
        """ Register AWS
        :param arn_role: IAM role ARN required for assume role to the customer cloud account
        :param external_id: External ID required for assume role to the customer cloud account
        :param name: Cloud account given name. If not passed its automatically generated by some pattern.
        May be used only for CI, tests and developers environments. Should not be used in production"""

        method_url = self._api_root.settings.aws_cloud_accounts()
        request = {"name": name, "arn_role": arn_role, "external_id": external_id}

        resp = self.session.put(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        return resp

    def get_account_template_url(self, external_id: str):
        """ Register AWS
        :param external_id: External ID required for assume role to the customer cloud account"""

        method_url = "{}?external_id={}".format(
            self._api_root.settings.aws_template(), external_id
        )
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        template_json = json.loads(resp.text)
        return template_json

    def unregister_aws_account(self, cloud_account_name: str):
        method_url = self._api_root.settings.aws_cloud_account_by_name(
            cloud_account_name
        )
        resp = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def unregister_azure_account(self, cloud_account_name: str):
        method_url = self._api_root.settings.azure_cloud_account_by_name(
            cloud_account_name
        )
        resp = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def add_aws_s3_artifacts_repo(self, account_name: str, bucket_name: str):
        method_url = self._api_root.artifacts_repository.aws_s3_storage(
            space_name=self.space
        )
        request = {"account_name": account_name, "bucket_name": bucket_name}
        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def add_azure_artifact_repository(self, account_name: str, storage_name: str):
        method_url = self._api_root.artifacts_repository.azure_storage(
            space_name=self.space
        )
        request = {"account_name": account_name, "storage_name": storage_name}
        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def get_artifact_repository(self):
        method_url = self._api_root.artifacts_repository.artifact_repos(
            space_name=self.space
        )
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        return Converters.create_artifact_repo_response(json.loads(res.text))

    def get_artifact_repo_storage(self, cloud_account: str):
        method_url = self._api_root.artifacts_repository.artifact_repos_by_cloud_account_name(
            cloud_account_name=cloud_account, space_name=self.space
        )
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        return json.loads(res.text)

    def remove_artifact_repository(self):
        method_url = self._api_root.artifacts_repository.artifact_repos(
            space_name=self.space
        )
        res = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def create_long_token(self) -> TokenResponse:
        method_url = self._api_root.token.long_token()
        resp = self.session.post(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        token_json = json.loads(resp.text)
        return Converters.create_token_response(token_json)

    def revoke_long_token(self, long_token: str):
        method_url = self._api_root.token.revoke_long_token()
        self.session.add_header("Authorization", "Bearer {}".format(long_token))
        resp = self.session.post(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def list_blueprints(
            self, exclude_samples=False, deployment_type: str = None
    ) -> List[BlueprintResponse]:
        params = {}
        if deployment_type:
            params["type"] = deployment_type
        method_url = self._api_root.blueprint.blueprints_by_space_name(self.space)
        resp = self.session.get(url=method_url, params=params)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        blueprints_json = json.loads(resp.text)
        all_blueprints = [
            Converters.create_blueprint_response(blueprint)
            for blueprint in blueprints_json
        ]
        if exclude_samples:
            all_blueprints = [
                blueprint for blueprint in all_blueprints if not blueprint.is_sample
            ]
        return all_blueprints

    def list_space_users(self) -> List[UserPermittedToSpaceResponse]:
        method_url = self._api_root.spaces.space_users(self.space)
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        users_json = json.loads(resp.text)
        return [
            Converters.create_user_permitted_to_space_response(user)
            for user in users_json
        ]

    def publish_blueprint_in_catalog(self, blueprint_name: str):
        method_url = self._api_root.catalog.catalog(space_name=self.space)
        request = {"blueprint_name": blueprint_name}
        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def list_blueprint_files(
            self, blueprint_name: str, branch: str
    ) -> List[BlueprintFileResponse]:
        method_url = self._api_root.blueprint.blueprint_files(
            space_name=self.space, blueprint_name=blueprint_name, branch=branch
        )
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        files = json.loads(resp.text)
        return [Converters.create_blueprint_file_response(file) for file in files]

    def list_blueprints_in_catalog(self) -> List[CatalogForGetAllResponse]:
        method_url = self._api_root.catalog.catalog(space_name=self.space)
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        blueprints_json = json.loads(resp.text)
        return [
            Converters.create_catalog_blueprint_response(blueprint)
            for blueprint in blueprints_json
        ]

    def unpublish_blueprint_in_catalog(self, blueprint_name: str):
        method_url = self._api_root.catalog.blueprint_in_catalog(
            space_name=self.space, blueprint_name=blueprint_name
        )
        resp = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def get_blueprint_details_in_catalog(
            self, blueprint_name: str
    ) -> CatalogForGetResponse:
        method_url = self._api_root.catalog.blueprint_in_catalog(
            space_name=self.space, blueprint_name=blueprint_name
        )
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        blueprint = json.loads(resp.text)
        return Converters.create_catalog_blueprint_full_response(blueprint)

    def list_sandboxes(self, retry: bool = True, **kwargs) -> List[SandboxResponseLean]:
        """
       :param retry: bool
       :param kwargs:  filter: str(automation/all/my),
                       sandbox_name: str,
                       count: int
       """

        method_url = self._api_root.sandbox.sandboxes()
        resp = self.session.get(url=method_url, params=kwargs)
        if resp.status_code in [408, 429]:
            if retry:
                time.sleep(30)
                return self.list_sandboxes(False, **kwargs)
            raise TimeoutError()
        GatewayUtils.handle_response(resp, return_codes=[200])
        result = json.loads(resp.text)
        return [
            Converters.create_sandbox_response_list_item(sandbox) for sandbox in result
        ]

    def list_productions(self, retry: bool = True) -> List[ProductionResponseLean]:
        url = self._api_root.production.productions()
        response = self.session.get(url=url)
        if response.status_code in [408, 429]:
            if retry:
                time.sleep(30)
                return self.list_productions(False)
            raise TimeoutError()
        GatewayUtils.handle_response(response, return_codes=[200])
        json_result = json.loads(response.text)
        return [
            Converters.create_production_response_list_item(item)
            for item in json_result
        ]

    def start_production(self, blueprint_name: str, artifacts: dict = None, inputs=None, compute_availability=None):
        url = self._api_root.production.productions()
        response = self.session.post(
            url=url,
            json={
                "blueprint_name": blueprint_name,
                "artifacts": artifacts if artifacts else {},
                "inputs": inputs if inputs else {},
                "compute_availability": compute_availability,
            },
        )
        GatewayUtils.handle_response(response=response, return_codes=[202])
        json_result = json.loads(response.text)
        return CreateProductionResponse(production_id=json_result["id"])

    def start_production_green(self,
                               production_id: str,
                               artifacts: dict = None,
                               inputs=None,
                               compute_availability: str = None):
        url = self._api_root.production.green_by_id(production_id=production_id)
        response = self.session.post(url=url, json={
            "artifacts": artifacts if artifacts else {},
            "inputs": inputs if inputs else {},
            "compute_availability": compute_availability
        })
        GatewayUtils.handle_response(response=response, return_codes=[202])
        json_result = json.loads(response.text)
        return CreateProductionResponse(production_id=json_result["id"])

    def update_production_debugging_service(self, production_id: str,
                                            environment: ProductionEnvironment,
                                            value: DebuggingServiceValue):
        if environment == ProductionEnvironment.BLUE:
            url = f'{self._api_root.production.blue_debugging_service(production_id=production_id)}'
        elif environment == ProductionEnvironment.GREEN:
            url = f'{self._api_root.production.green_debugging_service(production_id=production_id)}'
        else:
            raise ValueError(f'Unknown environment "{environment}"')

        response = self.session.put(url=f'{url}?value={value.value}')
        GatewayUtils.handle_response(response=response, return_codes=[200, 202])

    def expose_green(self, production_id: str, exposure_value: int):
        url = self._api_root.production.expose_green(production_id=production_id, exposure_value=exposure_value)
        response = self.session.put(url=url)
        GatewayUtils.handle_response(response=response, return_codes=[200, 202])

    def promote_green(self, production_id: str):
        url = self._api_root.production.promote_green(production_id=production_id)
        response = self.session.put(url=url)
        GatewayUtils.handle_response(response=response, return_codes=[200, 202])

    def start_sandbox(
            self, sandbox_name: str, blueprint_name: str, **kwargs
    ) -> CreateSandboxResponse:
        """
        :param sandbox_name: str
        :param blueprint_name: str
        :param kwargs:  artifacts: dict,
                        inputs: dict,
                        scheduled_end_time: datetime,
                        automation: bool,
                        duration: timedelta,
                        compute_availability: str,
                        lazy_load_artifacts: bool,
                        lazy_load_artifacts_timeout: int
        """
        method_url = self._api_root.sandbox.sandboxes()
        scheduled_end_time = (
            datetime.isoformat(kwargs.get("scheduled_end_time"))
            if kwargs.get("scheduled_end_time")
            else None
        )
        duration = duration_isoformat(kwargs.get("duration")) if kwargs.get("duration") else None
        resp = self.session.post(
            url=method_url,
            json={
                "blueprint_name": blueprint_name,
                "sandbox_name": sandbox_name,
                "artifacts": kwargs.get("artifacts", {}),
                "inputs": kwargs.get("inputs", {}),
                "automation": kwargs.get("automation", False),
                "scheduled_end_time": scheduled_end_time,
                "duration": duration,
                "compute_availability": kwargs.get("compute_availability"),
                "lazy_load_artifacts": kwargs.get("lazy_load_artifacts", False),
                "lazy_load_artifacts_timeout": kwargs.get("lazy_load_artifacts_timeout", 0),
            },
        )
        GatewayUtils.handle_response(response=resp, return_codes=[202])
        result = json.loads(resp.text)
        return CreateSandboxResponse(sandbox_id=result["id"])

    def end_sandbox(
            self,
            sandbox_id: str,
            retry: bool = True
    ):
        method_url = self._api_root.sandbox.sandbox_by_id(sandbox_id=sandbox_id)
        resp = self.session.delete(url=method_url)

        if resp.status_code in [408, 429, 504]:
            if retry:
                time.sleep(30)  # need to make sure that the next call will not use the cached timedout error
                self.end_sandbox(sandbox_id, False)
            raise TimeoutError()

        GatewayUtils.handle_response(response=resp, return_codes=[202])

    def end_production(self, production_id: str):
        method_url = self._api_root.production.production_by_id(
            production_id=production_id
        )
        resp = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[202])

    def end_production_green(self, production_id: str):
        method_url = self._api_root.production.green_by_id(production_id=production_id)
        resp = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[202])

    def get_sandbox_details(
            self, sandbox_id: str, retry: bool = True
    ) -> Optional[SandboxResponse]:
        method_url = self._api_root.sandbox.sandbox_by_id(sandbox_id=sandbox_id)
        resp = self.session.get(url=method_url)
        if resp.status_code == 404:
            return None
        if resp.status_code in [408, 429]:
            if retry:
                time.sleep(30)
                return self.get_sandbox_details(sandbox_id, False)
            raise TimeoutError()

        GatewayUtils.handle_response(response=resp, return_codes=[200])
        result = json.loads(resp.text)
        sandbox_response = Converters.create_sandbox_response(result)
        return sandbox_response

    def get_production_details(
            self, production_id: str, retry: bool = True) \
            -> Optional[ProductionBlueResponse]:
        url = self._api_root.production.production_by_id(production_id)
        response = self.session.get(url=url)
        if response.status_code == 404:
            return None
        if response.status_code in [408, 429]:
            if retry:
                time.sleep(30)
                return self.get_production_details(production_id, False)
            raise TimeoutError()

        GatewayUtils.handle_response(response=response, return_codes=[200])
        json_result = json.loads(response.text)
        production_response = Converters.create_production_blue_response(json_result)
        return production_response

    def get_production_green_details(
            self,
            production_id: str,
            retry: bool = True
    ) -> Optional[ProductionGreenResponse]:
        url = self._api_root.production.green_by_id(production_id)
        response = self.session.get(url=url)
        if response.status_code == 404:
            return None
        if response.status_code in [408, 429]:
            if retry:
                time.sleep(30)
                return self.get_production_green_details(production_id, False)
            raise TimeoutError()

        GatewayUtils.handle_response(response=response, return_codes=[200])
        json_result = json.loads(response.text)
        production_response = Converters.create_production_green_response(json_result)
        return production_response

    def add_repository_to_space(
            self,
            repository_details: BlueprintRepositoryDetails,
            deployment_type: str = None,
            wait_for_cache_refresh: bool = False,
    ):
        method_url = self._api_root.spaces.space_repositories(space_name=self.space)
        request = {
            "repository_url": repository_details.repository_url,
            "access_token": repository_details.access_token,
            "repository_type": repository_details.repository_type,
            "type": deployment_type,
        }
        resp = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

        if wait_for_cache_refresh:
            Utils.wait_for(
                func=lambda: (not self.list_blueprints(exclude_samples=True) is False),
                interval_sec=5,
                max_retries=24,
                subject="blueprints ready",
            )

    def remove_repository_from_space(self, wait_for_cache_refresh=False):
        method_url = self._api_root.spaces.space_repositories(space_name=self.space)
        resp = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

        if wait_for_cache_refresh:
            Utils.wait_for(
                func=lambda: (not self.list_blueprints(exclude_samples=True) is True),
                interval_sec=5,
                max_retries=24,
                subject="blueprints removed",
            )

    def get_tfstate_file(self, sandbox_id: str, service_name: str) -> bytes:
        method_url = self._api_root.sandbox.sandbox_tfstate(sandbox_id=sandbox_id, service_name=service_name)
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        return resp.content

    def validate_blueprint(self, blueprint: str, branch: str = None) -> bool:
        method_url = "{base}?blueprint={blueprint}&branch={branch}".format(
            base=self._api_root.blueprint_validation.blueprint_validation_by_space_name(
                space_name=self.space
            ),
            blueprint=blueprint,
            branch=branch if branch else "master",
        )
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        if resp.json() == {"errors": []}:
            return True
        return resp.json()

    def invite_user(self, invites: CreateInvitationsRequest):
        method_url = self._api_root.account.invitations()
        resp = self.session.post(url=method_url, json=invites.__dict__)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def get_invites(self, space_name: str = None) -> List[UserInvitationResponse]:
        method_url = self._api_root.account.account_invitations(space=space_name)
        resp = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=resp, return_codes=[200])
        result = json.loads(resp.text)
        return [Converters.create_user_invitation_response(x) for x in result]

    def test_invite_exists(self, secret: str):
        method_url = self._api_root.account.account_signup_by_secret(secret=secret)
        resp = self.session.get(url=method_url)
        return resp.status_code

    def remove_invites(self, emails: List[str]):
        method_url = self._api_root.account.account_invitations()
        req = {"emails": emails}
        resp = self.session.delete(url=method_url, json=req)
        GatewayUtils.handle_response(response=resp, return_codes=[200])

    def list_repositories(
            self, repository_type: str = None
    ) -> List[RepositoryResponse]:
        params = {}
        if repository_type:
            params["type"] = repository_type
        url = self._api_root.spaces.space_repositories(space_name=self.space)
        response = self.session.get(url=url, params=params)
        GatewayUtils.handle_response(response=response, return_codes=[200])
        json_result = json.loads(response.text)
        return [Converters.create_repository_response(x) for x in json_result]

    def update_scheduled_end_time(self, sandbox_id: str, scheduled_end_time: datetime):
        url = "{base}?value={end_time}".format(
            base=self._api_root.sandbox.sandbox_scheduled_end_time(
                sandbox_id=sandbox_id
            ),
            end_time=quote(scheduled_end_time.isoformat()),
        )
        response = self.session.put(url=url)
        GatewayUtils.handle_response(response=response, return_codes=[200])

    def turn_on_debugging_service(self, sandbox_id: str):
        self.update_debugging_service(sandbox_id=sandbox_id, value=DebuggingServiceValue.ON)

    def turn_off_debugging_service(self, sandbox_id: str):
        self.update_debugging_service(sandbox_id=sandbox_id, value=DebuggingServiceValue.OFF)

    def update_debugging_service(self, sandbox_id: str, value: DebuggingServiceValue):
        url = self._api_root.sandbox.sandbox_debugging_service(sandbox_id=sandbox_id)
        response = self.session.put(url=f'{url}?value={value.value}')
        GatewayUtils.handle_response(response=response, return_codes=[200, 202])

    def get_space_achievements(self) -> dict:
        url = self._api_root.achievements.achievements(space_name=self.space)
        response = self.session.get(url=url)
        GatewayUtils.handle_response(response, [200])
        return json.loads(response.text)

    def create_space(self, space_name: str, cloud_accounts: []):
        url = self._api_root.spaces.spaces()
        request = {"name": space_name, "cloud_accounts": cloud_accounts}

        response = self.session.post(url=url, json=request)
        GatewayUtils.handle_response(response=response, return_codes=[200])

    def delete_space(self, space_name: str):
        url = self._api_root.spaces.space_by_name(space_name=space_name)
        response = self.session.delete(url=url)
        GatewayUtils.handle_response(response=response, return_codes=[200])

    def get_space(self, name: str) -> GetSpaceResponse:
        url = self._api_root.spaces.space_by_name(space_name=name)
        res = self.session.get(url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        return GetSpaceResponse(json.loads(res.text))

    def update_space(self, space: str, update_space_request: UpdateSpaceRequest):
        url = self._api_root.spaces.space_by_name(space_name=space)
        response = self.session.put(url=url, json=update_space_request.__dict__)
        GatewayUtils.handle_response(response=response, return_codes=[200])

    def get_space_roles(self) -> List[RoleListItemResponse]:
        url = self._api_root.settings.space_roles()
        response = self.session.get(url=url)
        GatewayUtils.handle_response(response=response, return_codes=[200])
        roles_json = json.loads(response.text)
        return [Converters.create_role_list_item_response(role) for role in roles_json]

    def get_account_roles(self) -> List[RoleListItemResponse]:
        url = self._api_root.settings.account_roles()
        response = self.session.get(url=url)
        GatewayUtils.handle_response(response=response, return_codes=[200])
        roles_json = json.loads(response.text)
        return [Converters.create_role_list_item_response(role) for role in roles_json]

    def remove_cloud_account_from_space(self, cloud_account: str):
        method_url = self._api_root.spaces.space_cloud_account(
            self.space, cloud_account
        )
        res = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def add_cloud_account_to_space(self, cloud_account: str):
        method_url = self._api_root.spaces.space_cloud_accounts(self.space)
        res = self.session.post(url=method_url, json={"name": cloud_account})
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def get_cloud_accounts_under_space(self) -> List[CloudAccountResponse]:
        method_url = self._api_root.spaces.space_cloud_accounts(self.space)
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        return [
            Converters.create_cloud_account_response(x) for x in json.loads(res.text)
        ]

    def get_account_users(self) -> List[UserForAllUsersResponse]:
        method_url = self._api_root.account.account_users()
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        users_json = json.loads(res.text)
        return [Converters.create_user_for_all_users_response(x) for x in users_json]

    def get_space_permissions(self) -> List[str]:
        method_url = self._api_root.spaces.user_permissions(self.space)
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        return json.loads(res.text)

    def delete_account(self, account_name: str):
        method_url = self._api_root.account.delete_account(account_name)
        res = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        return res.text

    def contact_me(self, first_name: str, last_name: str, email: str, phone: str):
        method_url = self._api_root.account.contact_me()
        request = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone
        }
        res = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def add_user_to_space(self, user_email: str, space_role: str):
        method_url = self._api_root.spaces.space_users(self.space)
        request = {"email": user_email, "space_role": space_role}
        res = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def update_user_space_role(self, user_email: str, space_role: str):
        method_url = self._api_root.spaces.user_space_role(self.space, user_email, space_role)
        res = self.session.put(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def remove_user_from_space(self, user_email: str):
        method_url = self._api_root.spaces.space_user(self.space, user_email)
        res = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def update_user_account_role(self, user_email: str, account_role: str):
        method_url = self._api_root.account.account_user_account_role_value(user_email, account_role)
        res = self.session.put(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def remove_user_account_role(self, user_email: str):
        method_url = self._api_root.account.account_user_account_role(user_email)
        res = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def get_access_url_by_link(self, access_link: AccessLink) -> str:
        method_url = f"{self.api_address}{access_link.link}"
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        res_json = json.loads(res.text)
        return res_json['url']

    def get_access_url_by_params(self, sandbox_id: str, instance_id: str, protocol: str) -> str:
        method_url = self._api_root.qualiy.connect(sandbox_id=sandbox_id, instance_id=instance_id, protocol=protocol)
        res = self.session.get(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])
        res_json = json.loads(res.text)
        return res_json['url']

    def delete_user(self, user_email: str):
        method_url = self._api_root.account.account_user(user_email)
        res = self.session.delete(url=method_url)
        GatewayUtils.handle_response(response=res, return_codes=[200])

    def add_artifactory_repo(self,
                             server_url: str,
                             artifactory_username: str,
                             api_key: str):
        method_url = self._api_root.artifacts_repository.artifactory(space_name=self.space)
        request = {
            "server_url": server_url,
            "artifactory_username": artifactory_username,
            "api_key": api_key
        }
        response = self.session.post(url=method_url, json=request)
        GatewayUtils.handle_response(response=response,
                                     return_codes=[200])

    def get_cost_breakdown(self, frm: datetime, until: datetime, criteria: str = 'blueprint') -> dict:
        url = self._api_root.cost.breakdown(space_name=self.space, frm=frm, until=until, criteria=criteria)
        response = self.session.get(url=url)
        GatewayUtils.handle_response(response, [200])
        return json.loads(response.text)

    def get_cost_usage(self, date: datetime) -> dict:
        url = self._api_root.cost.usage(space_name=self.space, date=date)
        response = self.session.get(url=url)
        GatewayUtils.handle_response(response, [200])
        return json.loads(response.text)

    def post_request(self, url: str, request_json: dict, return_codes: List = None):
        return_codes = return_codes or [200]
        response = self.session.post(url=url, json=request_json)
        GatewayUtils.handle_response(response=response,
                                     return_codes=return_codes)

    def set_account_sso_enabled(self, account_name: str, enabled: bool):
        sso_enabled_url = self._api_root.account.set_sso_enabled(account_name)
        self.post_request(sso_enabled_url, {"enabled": enabled}, return_codes=[200])


class SandboxesHandler:
    def __init__(self):
        self.sandboxes_set = set()

    def add_sandbox(self, sandbox_id):
        self.sandboxes_set.add(sandbox_id)
        print("Sandbox {id} added to cleaner".format(id=sandbox_id))

    def remove_sandbox(self, sandbox_id):
        self.sandboxes_set.remove(sandbox_id)
        print("Sandbox {id} removed from cleaner".format(id=sandbox_id))


class SandboxCleaner:
    def __init__(self, client: Colony, end_on_exception=True):
        self.end_on_exception = end_on_exception
        self.client = client
        self.sandboxes = SandboxesHandler()
        self.space = self.client.space

    def __enter__(self):
        return self.sandboxes

    def __exit__(self, exc_type, exc_val: str, exc_tb):
        for sandbox in self.sandboxes.sandboxes_set:
            if exc_type is MaxRetriesException:
                print(f"Sandbox {sandbox} failed on timeout")
            elif exc_type is SandboxNotFound:
                print(f"Sandbox {sandbox} failed on not found")
            else:
                if self.end_on_exception:
                    print("Sandbox {} is being removed by cleaner".format(sandbox))
                    self.client.end_sandbox(sandbox_id=sandbox)


class ProductionCleaner:
    def __init__(self, client: Colony):
        self.client = client
        self.ids = []
        self.space = self.client.space

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for production_id in self.ids:
            print("Production {} is being removed by cleaner".format(production_id))

            self.client.end_production(production_id=production_id)

    def add(self, production_id):
        self.ids.append(production_id)
        print("Production {id} added to cleaner".format(id=production_id))

    def remove(self, production_id):
        self.ids.remove(production_id)
        print("Production {id} removed from cleaner".format(id=production_id))
