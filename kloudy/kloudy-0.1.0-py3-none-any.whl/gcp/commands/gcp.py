import click
import texttable as tt
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials


@click.group()
def gcp():
    """Google Cloud SubGroup"""
    pass


# ---------------------------------------------- Compute SubGroup ----------------------------------------------


@gcp.group()
def compute():
    """GCP compute engine sub-group"""
    pass


@compute.group()
def list():
    """list GCP Compute instances information"""
    pass


@list.command()
@click.option('--project', required=True, type=str)
@click.option('--zone', required=True, type=str)
def instances(project, zone):
    """list GCP Compute instances information"""
    instance_name_list = []
    instance_status_list = []
    instance_zone_list = []
    instance_private_ip_list = []
    instance_disk_list = []
    instance_service_account_list = []

    credentials = GoogleCredentials.get_application_default()

    service = discovery.build('compute', 'v1', credentials=credentials)

    request = service.instances().list(project=project, zone=zone)
    while request is not None:
        response = request.execute()

        for instance in response['items']:
            instance_name_list.append(instance['name'])
            instance_status_list.append(instance['status'])
            instance_zone_list.append(instance['zone'])
            instance_private_ip_list.append(instance['networkInterfaces'][0]['networkIP'])
            instance_disk_list.append(instance['disks'][0]['diskSizeGb'])
            instance_service_account_list.append(instance['serviceAccounts'][0]['email'])
        request = service.instances().list_next(previous_request=request, previous_response=response)

    tab = tt.Texttable(max_width=170)
    headings = ['Name', 'State', 'Zone', 'PrivateIp', 'DiskSize', 'ServiceAccount']
    tab.header(headings)
    for row in tuple(zip(instance_name_list, instance_status_list, instance_zone_list, instance_private_ip_list,
                         instance_disk_list, instance_service_account_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


# ---------------------------------------------- Project SubGroup ----------------------------------------------


@gcp.group()
def project():
    """GCP project sub-group"""
    pass


@project.group()
def list():
    """list GCP project related information"""
    pass


@list.command()
# ToDo Project Number format gets changed. Needs fix.
def projects():
    """list GCP Projects information"""
    project_name_list = []
    project_id_list = []
    project_state_list = []
    project_creation_time_list = []
    project_number_list = []

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

    request = service.projects().list()
    response = request.execute()

    for project in response.get('projects', []):
        project_name_list.append(project['name'])
        project_id_list.append(project['projectId'])
        project_state_list.append(project['lifecycleState'])
        project_creation_time_list.append(project['createTime'])
        project_number_list.append(project['projectNumber'])

    request = service.projects().list_next(previous_request=request, previous_response=response)

    tab = tt.Texttable(max_width=200)
    headings = ['Name', 'ProjectId', 'State', 'ProjectNumber', 'CreationTime']
    tab.header(headings)
    for row in tuple(zip(project_name_list, project_id_list, project_state_list,
                         project_number_list, project_creation_time_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)
