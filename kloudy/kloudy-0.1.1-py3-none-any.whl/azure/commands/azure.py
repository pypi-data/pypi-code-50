import os

import click
import texttable as tt
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient


@click.group()
def azure():
    """Azure Cloud Provider"""
    pass


# ---------------------------------------------- Virtual Machines SubGroup ---------------------------------------------


@azure.group()
def resource_groups():
    """Manage Azure Resource Groups"""
    pass


@resource_groups.group()
def list():
    """list azure resource groups"""
    pass


@list.command()
def all():
    """list all the resource groups in your subscription"""

    azure_resource_group_name_list = []
    azure_resource_group_location_list = []
    azure_resource_group_subscription_id_list = []

    subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID')
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )
    client = ResourceManagementClient(credentials, subscription_id)

    for item in client.resource_groups.list():
        azure_resource_group_name_list.append(item.name)
        azure_resource_group_location_list.append(item.location)
        azure_resource_group_subscription_id_list.append(subscription_id)

    tab = tt.Texttable(max_width=140)
    headings = ['ResourceGroupName', 'ResourceGroupLocation', 'SubscriptionId']
    tab.header(headings)
    for row in tuple(zip(azure_resource_group_name_list, azure_resource_group_location_list,
                         azure_resource_group_subscription_id_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)
