from typing import Dict, Any
from aws_cdk.aws_cloudformation import CustomResource, CustomResourceProvider, ICustomResourceProvider
from aws_cdk.aws_iam import Role, CompositePrincipal, ServicePrincipal, PolicyDocument, PolicyStatement, Effect
from aws_cdk.aws_lambda import IFunction, Runtime, Code, Function
from aws_cdk.core import Stack, RemovalPolicy, Duration
from aws_ecs_service.package import package_root


class EcsService:
    """
    Class that manages ecs service resource.

    Read more about ecs service:
    https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html
    """
    def __init__(
            self,
            scope: Stack,
            id: str,
            on_create_action: Dict[str, Any],
            on_update_action: Dict[str, Any],
            on_delete_action: Dict[str, Any],
    ) -> None:
        """
        Constructor.

        :param scope: CloudFormation stack in which resources should be placed.
        :param id: Name (id) or prefix for resources.
        :param on_create_action: Create action arguments. Read more on:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_service
        :param on_update_action: Update action arguments. Read more on:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_service
        :param on_delete_action: Delete action arguments. Read more on:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_service
        """
        self.__role = Role(
            scope=scope,
            id=id + 'Role',
            role_name=id + 'Role',
            assumed_by=CompositePrincipal(
                ServicePrincipal("lambda.amazonaws.com"),
                ServicePrincipal("cloudformation.amazonaws.com")
            ),
            inline_policies={
                id + 'Policy': PolicyDocument(
                    statements=[
                        PolicyStatement(
                            actions=[
                                'ecs:createService',
                                'ecs:updateService',
                                'ecs:deleteService',
                                'ecs:describeServices',
                                'ecs:listServices',
                                'ecs:updateServicePrimaryTaskSet'
                            ],
                            effect=Effect.ALLOW,
                            resources=['*']
                        ),
                        PolicyStatement(
                            actions=[
                                "logs:CreateLogGroup",
                                "logs:CreateLogStream",
                                "logs:PutLogEvents"
                            ],
                            effect=Effect.ALLOW,
                            resources=['*']
                        ),
                    ]
                )
            },
            managed_policies=[]
        )

        self.__custom_backend = Function(
            scope=scope,
            id=id + 'Backend',
            code=Code.from_asset(
                path=package_root
            ),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            description=f'A custom resource backend to manage ecs {id} service.',
            function_name=id + 'Backend',
            memory_size=128,
            role=self.__role,
            timeout=Duration.seconds(900),
        )

        # noinspection PyTypeChecker
        provider: ICustomResourceProvider = CustomResourceProvider.from_lambda(self.__custom_backend)

        self.__custom_resource = CustomResource(
            scope=scope,
            id=id + 'CustomResource',
            provider=provider,
            removal_policy=RemovalPolicy.DESTROY,
            properties={
                'onCreate': on_create_action,
                'onUpdate': on_update_action,
                'onDelete': on_delete_action
            },
            resource_type='Custom::EcsService'
        )

        # Make sure that custom resource is deleted before lambda function backend.
        self.__custom_resource.node.add_dependency(self.__custom_backend)

    @property
    def arn(self) -> str:
        return self.__custom_resource.get_att('arn')

    @property
    def name(self) -> str:
        return self.__custom_resource.get_att('name')

    @property
    def backend(self) -> IFunction:
        return self.__custom_backend

    @property
    def custom_resource(self) -> CustomResource:
        return self.__custom_resource
