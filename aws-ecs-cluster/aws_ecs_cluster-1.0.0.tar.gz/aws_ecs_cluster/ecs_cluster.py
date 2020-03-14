from typing import Optional
from aws_cdk.aws_cloudformation import CustomResource, CustomResourceProvider, ICustomResourceProvider
from aws_cdk.aws_ec2 import IVpc
from aws_cdk.aws_ecs import Cluster, AddCapacityOptions, CloudMapNamespaceOptions
from aws_cdk.aws_iam import Role, CompositePrincipal, ServicePrincipal, PolicyDocument, PolicyStatement, Effect
from aws_cdk.aws_lambda import IFunction, Runtime, Code, Function
from aws_cdk.core import Stack, RemovalPolicy, Duration
from aws_ecs_cluster.package import package_root


class EcsCluster(Cluster):
    def __init__(
            self,
            scope: Stack,
            id: str,
            capacity: Optional[AddCapacityOptions] = None,
            cluster_name: Optional[str] = None,
            container_insights: Optional[bool] = None,
            default_cloud_map_namespace: Optional[CloudMapNamespaceOptions] = None,
            vpc: Optional[IVpc] = None,
            **kwargs
    ) -> None:
        known_args = dict(
            scope=scope,
            id=id,
            capacity=capacity,
            cluster_name=cluster_name,
            container_insights=container_insights,
            default_cloud_map_namespace=default_cloud_map_namespace,
            vpc=vpc
        )

        unknown_args = kwargs

        super().__init__(
            **{
                **known_args,
                **unknown_args
            }
        )

        self.__role = Role(
            scope=scope,
            id=cluster_name + 'CustomResourceRole',
            role_name=cluster_name + 'CustomResourceRole',
            assumed_by=CompositePrincipal(
                ServicePrincipal("lambda.amazonaws.com"),
                ServicePrincipal("cloudformation.amazonaws.com")
            ),
            inline_policies={
                cluster_name + 'CustomResourcePolicy': PolicyDocument(
                    statements=[
                        PolicyStatement(
                            actions=[
                                "ecs:ListClusters",
                                "ecs:ListContainerInstances",
                                "ecs:ListServices",
                                "ecs:ListTaskDefinitions",
                                "ecs:ListTasks",
                                "ecs:DescribeClusters",
                                "ecs:DescribeContainerInstances",
                                "ecs:DescribeServices",
                                "ecs:DescribeTaskDefinition",
                                "ecs:DescribeTasks",
                                "ecs:CreateCluster",
                                "ecs:DeleteCluster",
                                "ecs:DeleteService",
                                "ecs:DeregisterContainerInstance",
                                "ecs:DeregisterTaskDefinition",
                                "ecs:StopTask",
                                "ecs:UpdateService",
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
            id=cluster_name + 'Deleter',
            code=Code.from_asset(
                path=package_root
            ),
            handler='index.handler',
            runtime=Runtime.PYTHON_3_6,
            description=f'A custom resource backend to delete ecs cluster ({cluster_name}) in the right way.',
            function_name=cluster_name + 'Deleter',
            memory_size=128,
            role=self.__role,
            timeout=Duration.seconds(900),
        )

        # noinspection PyTypeChecker
        provider: ICustomResourceProvider = CustomResourceProvider.from_lambda(self.__custom_backend)

        self.__custom_resource = CustomResource(
            scope=scope,
            id=cluster_name + 'CustomResource',
            provider=provider,
            removal_policy=RemovalPolicy.DESTROY,
            properties={
                'clusterName': cluster_name
            },
            resource_type='Custom::EmptyS3Bucket'
        )

        # Make sure that custom resource is deleted before lambda function backend.
        self.__custom_resource.node.add_dependency(self.__custom_backend)
        # Make sure that custom resource is deleted before the bucket.
        self.__custom_resource.node.add_dependency(self)

    @property
    def backend(self) -> IFunction:
        return self.__custom_backend

    @property
    def custom_resource(self) -> CustomResource:
        return self.__custom_resource
