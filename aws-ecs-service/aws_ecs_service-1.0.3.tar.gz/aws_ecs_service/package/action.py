import boto3
import logging

from botocore.exceptions import ClientError

try:
    from aws_ecs_service.package.response import Response
    from aws_ecs_service.package.fix_kwargs import fix_kwargs
except ImportError:
    # Lambda specific import.
    # noinspection PyUnresolvedReferences
    from response import Response
    # noinspection PyUnresolvedReferences
    from fix_kwargs import fix_kwargs


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Action:
    @staticmethod
    @fix_kwargs
    def create(**kwargs) -> Response:
        """
        Runs and maintains a desired number of tasks from a specified task definition.
        If the number of tasks running in a service drops below the desiredCount , Amazon ECS runs
        another copy of the task in the specified cluster. To update an existing service, see UpdateService.

        In addition to maintaining the desired count of tasks in your service, you can
        optionally run your service behind one or more load balancers. The load balancers
        distribute traffic across the tasks that are associated with the service.

        Read more:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.create_service

        :param kwargs: Create action arguments.

        :return: Response dictionary.
        """
        response = boto3.client('ecs').create_service(**kwargs)

        return Response(
            cluster=kwargs.get('cluster'),
            service_name=kwargs.get('serviceName'),
            success=True,
            metadata=response
        )

    @staticmethod
    @fix_kwargs
    def update(**kwargs) -> Response:
        """
        Modifies the parameters of a service.

        For services using the rolling update (ECS ) deployment controller, the desired count,
        deployment configuration, network configuration, or task definition used can be updated.

        For services using the blue/green (CODE_DEPLOY ) deployment controller, only the desired count,
        deployment configuration, and health check grace period can be updated using this API.
        If the network configuration, platform version, or task definition need to be updated,
        a new AWS CodeDeploy deployment should be created.

        Read more:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.update_service

        :param kwargs: Update action arguments.

        :return: Response dictionary.
        """
        try:
            response = boto3.client('ecs').update_service(**kwargs)
        except ClientError as ex:
            if ex.response['Error']['Code'] == 'InvalidParameterException':
                if 'codedeploy' in ex.response['Error']['Message'].lower():
                    # For services using the blue/green (CODE_DEPLOY ) deployment controller,
                    # only the desired count, deployment configuration, and health check grace period
                    # can be updated using this API. If the network configuration, platform version, or task definition
                    # need to be updated, a new AWS CodeDeploy deployment should be created.
                    kwargs = dict(
                        cluster=kwargs.get('cluster'),
                        service=kwargs.get('serviceName'),
                        desiredCount=kwargs.get('desiredCount'),
                        deploymentConfiguration=kwargs.get('deploymentConfiguration'),
                        healthCheckGracePeriodSeconds=kwargs.get('healthCheckGracePeriodSeconds'),
                    )

                    response = boto3.client('ecs').update_service(**kwargs)
                else:
                    raise
            elif ex.response['Error']['Code'] == 'ServiceNotActiveException':
                # We can not update ecs service if it is inactive.
                response = {'status': 'ServiceNotActiveException'}
            elif ex.response['Error']['Code'] == 'ServiceNotFoundException':
                # If for some reason service was not found - don't update and return.
                response = {'status': 'ServiceNotFoundException'}
            else:
                raise

        return Response(
            cluster=kwargs.get('cluster'),
            service_name=kwargs.get('serviceName'),
            success=True,
            metadata=response
        )

    @staticmethod
    @fix_kwargs
    def delete(**kwargs) -> Response:
        """
        Deletes a specified service within a cluster. You can delete a service if you have no
        running tasks in it and the desired task count is zero. If the service is actively
        maintaining tasks, you cannot delete it, and you must update the service to a desired
        task count of zero. For more information, see UpdateService.

        Read more:
        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecs.html#ECS.Client.delete_service

        :param kwargs: Delete action arguments.

        :return: Response dictionary.
        """
        try:
            logger.info('Making ecs desired count 0...')
            boto3.client('ecs').update_service(
                cluster=kwargs.get('cluster'),
                service=kwargs.get('serviceName'),
                desiredCount=0,
            )
        except ClientError as ex:
            logger.error(
                f'Failed to set desired count to 0. Reason: {repr(ex)}, {ex.response}. '
                f'Ignoring exception and trying to delete ecs service anyways.'
            )

        logger.info('Deleting service...')
        response = boto3.client('ecs').delete_service(**kwargs)

        return Response(
            cluster=kwargs.get('cluster'),
            service_name=kwargs.get('serviceName'),
            success=True,
            metadata=response
        )
