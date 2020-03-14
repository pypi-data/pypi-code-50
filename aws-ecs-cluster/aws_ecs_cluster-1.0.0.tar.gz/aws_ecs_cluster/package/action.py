import time
import boto3
import logging

from typing import Any, Dict
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Action:
    @staticmethod
    def create(**kwargs) -> Dict[str, Any]:
        logger.info('Not doing anything since this backend only deletes the cluster.')
        return {'status': 'skipped'}

    @staticmethod
    def update(**kwargs) -> Dict[str, Any]:
        logger.info('Not doing anything since this backend only deletes the cluster.')
        return {'status': 'skipped'}

    @staticmethod
    def delete(**kwargs: Dict[str, Any]) -> Dict[str, Any]:
        cluster = kwargs.get('clusterName', kwargs.get('ClusterName', kwargs.get('cluster_name')))
        client = boto3.client('ecs')

        """
        Instruct auto-scaling to shrink to zero.
        """

        try:
            services = client.list_services(
                cluster=cluster,
            )['serviceArns']
        except ClientError as ex:
            logging.error(f'Failed to list services reason: {repr(ex)}, {ex.response}.')
            services = []
        except Exception as ex:
            logging.error(f'Failed to list services reason: {repr(ex)}.')
            services = []

        for service in services:
            try:
                client.update_service(
                    cluster=cluster,
                    service=service,
                    desiredCount=0,
                )
            except ClientError as ex:
                logging.error(f'Failed to update service {service}, reason: {repr(ex)}, {ex.response}.')
            except Exception as ex:
                logging.error(f'Failed to update service {service}, reason: {repr(ex)}.')

        """
        Stop all tasks.
        """

        try:
            tasks = client.list_tasks(
                cluster=cluster
            )['taskArns']
        except ClientError as ex:
            logging.error(f'Failed to list tasks reason: {repr(ex)}, {ex.response}.')
            tasks = []
        except Exception as ex:
            logging.error(f'Failed to list tasks reason: {repr(ex)}.')
            tasks = []

        for task in tasks:
            try:
                client.stop_task(
                    cluster=cluster,
                    task=task,
                    reason=f'Cluster {cluster} is being deleted. Killing all tasks.'
                )
            except ClientError as ex:
                logging.error(f'Failed to stop task {task}, reason: {repr(ex)}, {ex.response}.')
            except Exception as ex:
                logging.error(f'Failed to stop task {task}, reason: {repr(ex)}.')

        """
        Deregister all instances.
        """
        ecs_instances = [None]
        retries_left = 6

        while len(ecs_instances) > 0 < retries_left:
            try:
                ecs_instances = client.list_container_instances(
                    cluster=cluster
                )['containerInstanceArns']
            except ClientError as ex:
                logging.error(f'Failed to list container instances, reason: {repr(ex)}, {ex.response}.')
            except Exception as ex:
                logging.error(f'Failed to list container instances, reason: {repr(ex)}.')

            logging.info(f'Instances to deregister: {ecs_instances}.')

            for instance in ecs_instances:
                try:
                    client.deregister_container_instance(
                        cluster=cluster,
                        containerInstance=instance,
                        force=True
                    )
                except ClientError as ex:
                    logging.error(f'Failed to deregister {instance}, reason: {repr(ex)}, {ex.response}.')
                except Exception as ex:
                    logging.error(f'Failed to deregister {instance}, reason: {repr(ex)}.')

            retries_left -= 1
            logging.info('Sleeping for 10 seconds.')
            time.sleep(10)

        """
        Delete services.
        """
        try:
            services = client.list_services(
                cluster=cluster,
            )['serviceArns']
        except ClientError as ex:
            logging.error(f'Failed to list services reason: {repr(ex)}, {ex.response}.')
            services = []
        except Exception as ex:
            logging.error(f'Failed to list services reason: {repr(ex)}.')
            services = []

        for service in services:
            try:
                client.delete_service(
                    cluster=cluster,
                    service=service,
                    force=True
                )
            except ClientError as ex:
                logging.error(f'Failed to delete service {service}, reason: {repr(ex)}, {ex.response}.')
            except Exception as ex:
                logging.error(f'Failed to delete service {service}, reason: {repr(ex)}.')

        """
        Delete cluster.
        """
        return client.delete_cluster(
            cluster=cluster
        )
