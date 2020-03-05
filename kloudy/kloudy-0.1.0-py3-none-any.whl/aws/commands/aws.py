import datetime
import json
import sys
from datetime import date, timedelta

import boto3
import botocore
import click
import texttable as tt

last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)
start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)


@click.group()
def aws():
    """AWS Cloud SubGroup"""
    pass


# ---------------------------------------------- Billing SubGroup ----------------------------------------------


@aws.group()
def billing():
    """Manage AWS Billing resources"""
    pass


@billing.group()
def list():
    """list AWS Billing resources"""
    pass


@list.command()
@click.option('--start-date', required=True, type=str, default=str(start_day_of_prev_month), show_default=True)
@click.option('--end-date', required=True, type=str, default=str(last_day_of_prev_month), show_default=True)
@click.option('--profile', required=False, show_default=True, default='default', type=str)
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str)
def monthly(start_date, end_date, profile, region):
    """list AWS account billing information"""
    try:
        start_date_list = []
        end_date_list = []
        total_list = []
        estimated_list = []
        unit_list = []
        # services_list = []
        boto3.setup_default_session(profile_name=profile, region_name=region)
        client = boto3.client('ce')
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date
            },
            Metrics=[
                'UnblendedCost'
            ],
            # GroupBy =[
            #     {'Type': 'DIMENSION', 'Key': 'LINKED_ACCOUNT'}
            #     # {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            # ],
            Granularity='MONTHLY'
        )
        for index, _cost in enumerate(response['ResultsByTime']):
            start_date_list.append(response['ResultsByTime'][index]['TimePeriod']['Start'])
            end_date_list.append(response['ResultsByTime'][index]['TimePeriod']['End'])
            # services_list.append(response['ResultsByTime'][index]['Groups'][index]['Keys'][1])
            total_list.append(response['ResultsByTime'][index]['Total']['UnblendedCost']['Amount'])
            unit_list.append(response['ResultsByTime'][index]['Total']['UnblendedCost']['Unit'])
        tab = tt.Texttable(max_width=140)
        headings = ['Start', 'End', 'Total', 'Unit']
        tab.header(headings)
        for row in tuple(zip(start_date_list, end_date_list, total_list, unit_list)):
            # print(row)
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                               f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


@list.command()
@click.option('--start-date', required=True, type=str, default=str(start_day_of_prev_month), show_default=True)
@click.option('--end-date', required=True, type=str, default=str(last_day_of_prev_month), show_default=True)
@click.option('--profile', required=False, show_default=True, default='default', type=str)
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str)
def monthly_by_service(start_date, end_date, profile, region):
    """list AWS account billing information"""
    try:
        start_date_list = []
        end_date_list = []
        total_list = []
        region_list = []
        unit_list = []
        services_list = []
        boto3.setup_default_session(profile_name=profile, region_name=region)
        client = boto3.client('ce')
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date
            },
            Metrics=[
                'UnblendedCost'
            ],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'},
                {'Type': 'DIMENSION', 'Key': 'REGION'}
            ],
            Granularity='MONTHLY'
        )
        for index, _cost in enumerate(response['ResultsByTime']):
            # services_list.append(response['ResultsByTime'][index]['Groups'][index]['Keys'][1])
            for index2, _group_by in enumerate(response['ResultsByTime'][index]['Groups']):
                start_date_list.append(response['ResultsByTime'][index]['TimePeriod']['Start'])
                end_date_list.append(response['ResultsByTime'][index]['TimePeriod']['End'])
                services_list.append(response['ResultsByTime'][index]['Groups'][index2]['Keys'][0])
                region_list.append(response['ResultsByTime'][index]['Groups'][index2]['Keys'][1])
                total_list.append(
                    response['ResultsByTime'][index]['Groups'][index2]['Metrics']['UnblendedCost']['Amount'])
                unit_list.append(response['ResultsByTime'][index]['Groups'][index2]['Metrics']['UnblendedCost']['Unit'])
        tab = tt.Texttable(max_width=150)
        headings = ['Start', 'End', 'Service', 'Region', 'Total', 'Unit']
        tab.header(headings)
        for row in tuple(zip(start_date_list, end_date_list, services_list, region_list, total_list, unit_list)):
            # print(row)
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                               f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


# ---------------------------------------------- CloudTrail SubGroup ----------------------------------------------


@aws.group()
def cloudtrail():
    """Manage AWS CloudTrail resources"""
    pass


@cloudtrail.group()
def list():
    """Print the resources information"""
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
@click.option('--interval', required=True, type=int, default=1, show_default=True, help='Enter interval in hours')
def lookup_events(profile, region, interval):
    """list CloudTrail events for a requested region"""
    duration = datetime.timedelta(hours=interval)
    event_name_list = []
    event_time_list = []
    event_user_list = []
    event_source_list = []
    event_region_list = []
    event_request_details_list = []
    event_source_ip_list = []
    end_time = datetime.datetime.now()
    start_time = end_time - duration

    def common():
        cloudtrail = boto3.client('cloudtrail')
        response = cloudtrail.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'ReadOnly',
                    'AttributeValue': 'false'
                },
            ],
            StartTime=start_time,
            EndTime=end_time)
        for index, _event in enumerate(response['Events']):
            event_name_list.append(response['Events'][index]['EventName'])
            event_time_list.append(response['Events'][index]['EventTime'])
            event_user_list.append(response['Events'][index]['Username'])
            event_source_list.append(response['Events'][index]['EventSource'])
            event_request_details_list.append(json.loads(response['Events'][index]['CloudTrailEvent'])
                                              ['requestParameters'])
            event_source_ip_list.append(json.loads(response['Events'][index]['CloudTrailEvent'])
                                        ['sourceIPAddress'])
            event_region_list.append(region)

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        all_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in all_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)
        # paginator = cloudtrail.get_paginator('lookup_events')
        # response_iterator = paginator.paginate(
        #   PaginationConfig={
        #       'MaxItems': 999,
        #       'PageSize': 50,
        #   }
        # )
        # result = response_iterator.build_full_result()
    tab = tt.Texttable(max_width=180)
    headings = ['Event', 'EventTime', 'User', 'EventSource', 'SourceIp', 'RequestDetails', 'Region']
    tab.header(headings)
    for row in tuple(
            zip(event_name_list, event_time_list, event_user_list, event_source_list, event_source_ip_list,
                event_request_details_list, event_region_list)):
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


# ---------------------------------------------- Ebs SubGroup ----------------------------------------------


@aws.group()
def ebs():
    """Manage AWS EBS resources"""
    pass


@ebs.group()
def list():
    """Print the resources information"""
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
# ToDo Add AZ in the output for EBS volume.
# ToDo Add filter to list only volumes that are in a requested state.
def volumes(profile, region):
    """list EC2 instances in current region"""
    ebs_volume_id_list = []
    ebs_volume_size_list = []
    ebs_volume_type_list = []
    ebs_volume_multi_attached_list = []
    ebs_volume_snapshot_id_list = []
    ebs_volume_encryption_list = []
    ebs_volume_creation_time_list = []
    ebs_volume_state_list = []
    ebs_volume_attachment_list = []
    ebs_volume_region_list = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_volumes()
        for index, _volume in enumerate(response['Volumes']):
            ebs_volume_id_list.append(response['Volumes'][index]['VolumeId'])
            ebs_volume_type_list.append(response['Volumes'][index]['VolumeType'])
            ebs_volume_size_list.append(response['Volumes'][index]['Size'])
            ebs_volume_snapshot_id_list.append(response['Volumes'][index]['SnapshotId'])
            if response['Volumes'][index]['Encrypted'] is True:
                ebs_volume_encryption_list.append('True')
            else:
                ebs_volume_encryption_list.append('False')
            if response['Volumes'][index]['MultiAttachEnabled'] is True:
                ebs_volume_multi_attached_list.append('True')
            else:
                ebs_volume_multi_attached_list.append('False')
            ebs_volume_creation_time_list.append(response['Volumes'][index]['CreateTime'])
            ebs_volume_state_list.append(response['Volumes'][index]['State'])
            if not response['Volumes'][index]['Attachments']:
                ebs_volume_attachment_list.append('Null')
            else:
                ebs_volume_attachment_list.append(response['Volumes'][index]['Attachments'][0]['InstanceId'])
            ebs_volume_region_list.append(region)

    client = boto3.client('ec2', region_name='us-east-1')
    ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    if region == 'all':
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()

        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)

    tab = tt.Texttable(max_width=180)
    headings = ['VolumeId', 'VolumeType', 'SizeInGb', 'AttachedTo', 'SnapshotId', 'Encrypted', 'MultiAttachEnabled',
                'State',
                'CreationTime', 'Region']
    tab.header(headings)
    for row in tuple(zip(ebs_volume_id_list, ebs_volume_type_list, ebs_volume_size_list, ebs_volume_attachment_list,
                         ebs_volume_snapshot_id_list,
                         ebs_volume_encryption_list, ebs_volume_multi_attached_list, ebs_volume_state_list,
                         ebs_volume_creation_time_list, ebs_volume_region_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
@click.option('--volume-id', required=True, type=str)
def volume_snapshot(volume_id, profile, region):
    """list EBS snapshot for a specific volume"""
    volume_snapshot_id_list = []
    volume_snapshot_state_list = []
    volume_snapshot_encryption_list = []
    volume_snapshot_progress_list = []
    volume_snapshot_start_time_list = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_snapshots(
            Filters=[
                {
                    'Name': 'volume-id',
                    'Values': [
                        volume_id,
                    ]
                },
            ]
        )
        for index, _snapshot in enumerate(response['Snapshots']):
            volume_snapshot_id_list.append(response['Snapshots'][index]['SnapshotId'])
            if response['Snapshots'][index]['Encrypted'] is not True:
                volume_snapshot_encryption_list.append('False')
            else:
                volume_snapshot_encryption_list.append('True')
            volume_snapshot_progress_list.append(response['Snapshots'][index]['Progress'])
            volume_snapshot_state_list.append(response['Snapshots'][index]['State'])
            volume_snapshot_start_time_list.append(response['Snapshots'][index]['StartTime'])
        tab = tt.Texttable(max_width=180)
        headings = ['SnapshotId', 'Encrypted', 'Progress', 'State', 'CreationTime']
        tab.header(headings)
        for row in tuple(zip(volume_snapshot_id_list, volume_snapshot_encryption_list, volume_snapshot_progress_list,
                             volume_snapshot_state_list, volume_snapshot_start_time_list)):
            # print(row)
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)

    try:
        boto3.setup_default_session(profile_name=profile, region_name=region)
        common()

    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


# ---------------------------------------------- EC2 SubGroup ----------------------------------------------


@aws.group()
def ec2():
    """Manage AWS EC2 resources"""
    pass


@ec2.group()
def list():
    """Print the resources information"""
    pass


@ec2.group()
def describe():
    """Describe the resources in more details"""
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
@click.option('--state', required=True, show_default=True, type=click.Choice(['all', 'running', 'stopped']),
              default='all')
@click.option('--csv-format', required=False, show_default=True, default='False', type=click.Choice(['True', 'False']))
def instances(profile, region, state, csv_format):
    """list EC2 instances in a requested region"""
    if region == 'all':
        # if state != 'all':
        #     click.echo("Invalid parameter combination specified. '--state' parameter with '--region all' parameter "
        #                "is not supported.")
        # else:
        instance_id_list = []
        instance_type_list = []
        instance_private_ip_list = []
        instance_image_id_list = []
        instance_vpc_id_list = []
        instance_subnet_id_list = []
        instance_state_list = []
        instance_root_volume_list = []
        instance_availability_zone_list = []
        instance_region_list = []
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]

        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
            conn = boto3.resource('ec2')
            if state == 'all':
                all_instances = conn.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running',
                                                                                                          'stopped']}])
            else:
                all_instances = conn.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': [state]}])
            for instance in all_instances:
                # if instance.state["Name"] == "running":
                instance_id_list.append(instance.id)
                instance_type_list.append(instance.instance_type)
                instance_private_ip_list.append(instance.private_ip_address)
                instance_image_id_list.append(instance.image_id)
                instance_vpc_id_list.append(instance.vpc_id)
                instance_subnet_id_list.append(instance.subnet_id)
                instance_state_list.append(instance.state['Name'])
                if not instance.block_device_mappings:
                    instance_root_volume_list.append('No Root Volume')
                else:
                    instance_root_volume_list.append(instance.block_device_mappings[0]['Ebs']['VolumeId'])
                instance_availability_zone_list.append(instance.placement['AvailabilityZone'])
                instance_region_list.append(region)
                # print(instance.id, instance.instance_type, region)

        if csv_format == 'True':
            with open(f'{profile}_ec2_instances.csv', 'w') as file:
                writer = csv.writer(file, lineterminator='\n')
                for row in zip(instance_id_list, instance_type_list, instance_state_list, instance_root_volume_list,
                               instance_private_ip_list, instance_image_id_list, instance_vpc_id_list,
                               instance_subnet_id_list, instance_availability_zone_list, instance_region_list):
                    writer.writerow(row)
        else:
            tab = tt.Texttable(max_width=180)
            headings = ['InstanceId', 'InstanceType', 'State', 'RootVolume', 'PrivateIp', 'AmiId', 'VpcId', 'SubnetId',
                        'AvailabilityZone', 'Region']
            tab.header(headings)
            for row in tuple(zip(instance_id_list, instance_type_list, instance_state_list, instance_root_volume_list,
                                 instance_private_ip_list, instance_image_id_list, instance_vpc_id_list,
                                 instance_subnet_id_list, instance_availability_zone_list, instance_region_list)):
                # print(row)
                tab.add_row(row)
            s = tab.draw()
            click.echo(s)
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)
        client = boto3.client('ec2')
        if state == 'all':
            response = client.describe_instances()
        else:
            response = client.describe_instances(
                Filters=[
                    {
                        'Name': 'instance-state-name',
                        'Values': [
                            state
                        ]
                    }
                ]
            )
        InstanceIds = []
        InstanceTypes = []
        InstancesPrivateIpAddress = []
        InstancesImageId = []
        InstancesVpcId = []
        InstancesSubnetId = []
        InstancesState = []
        InstancesRootVolume = []
        InstancesSecurityGroups = []
        InstancesAvailabilityZones = []
        for reservation in response["Reservations"]:
            for index, instance in enumerate(reservation["Instances"]):
                try:
                    InstanceIds.append(reservation["Instances"][index]["InstanceId"])
                    InstanceTypes.append(
                        reservation["Instances"][index]["InstanceType"])
                    InstancesPrivateIpAddress.append(
                        reservation["Instances"][index]["PrivateIpAddress"])
                    InstancesImageId.append(
                        reservation["Instances"][index]["ImageId"])
                    InstancesVpcId.append(
                        reservation["Instances"][index]["VpcId"])
                    InstancesSubnetId.append(
                        reservation["Instances"][index]["SubnetId"])
                    InstancesState.append(
                        reservation["Instances"][index]["State"]["Name"])
                    if not reservation["Instances"][index]["BlockDeviceMappings"]:
                        InstancesRootVolume.append('No Root Volume')
                    else:
                        InstancesRootVolume.append(
                            reservation["Instances"][index]["BlockDeviceMappings"][0]["Ebs"]["VolumeId"])
                    InstancesAvailabilityZones.append(reservation["Instances"][index]["Placement"]["AvailabilityZone"])
                    # if len(reservation["Instances"][index]["SecurityGroups"]) > 1:
                    #     for index,sg in enumerate(reservation["Instances"][index]["SecurityGroups"]):
                    #         print(index)
                    #         # print(reservation["Instances"][index]["SecurityGroups"])
                    #         InstancesSecurityGroups.append(reservation["Instances"][index]["SecurityGroups"][index]["GroupName"])
                    # else:
                    #     InstancesSecurityGroups.append(reservation["Instances"][index]["SecurityGroups"][index]["GroupName"])
                except KeyError:
                    pass
        if csv_format == 'True':
            # TODO user should be able to specify the csv file name.
            with open(f'{profile}_ec2_instances.csv', 'w') as file:
                writer = csv.writer(file, lineterminator='\n')
                for row in zip(InstanceIds, InstanceTypes, InstancesState, InstancesRootVolume,
                               InstancesPrivateIpAddress, InstancesImageId, InstancesVpcId, InstancesSubnetId,
                               InstancesAvailabilityZones):
                    writer.writerow(row)
        else:
            tab = tt.Texttable(max_width=180)
            headings = ['InstanceId', 'InstanceType', 'State', 'RootVolume', 'PrivateIp', 'AmiId', 'VpcId', 'SubnetId',
                        'AvailabilityZone']
            tab.header(headings)
            for row in tuple(
                    zip(InstanceIds, InstanceTypes, InstancesState, InstancesRootVolume, InstancesPrivateIpAddress,
                        InstancesImageId, InstancesVpcId, InstancesSubnetId, InstancesAvailabilityZones)):
                # print(row)
                tab.add_row(row)
            s = tab.draw()
            click.echo(s)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
def security_groups(profile, region):
    """list Security Groups in current region"""
    SecurityGroupNames = []
    SecurityGroupIds = []
    SecurityVpcIds = []
    try:
        boto3.setup_default_session(profile_name=profile, region_name=region)
        client = boto3.client('ec2')
        response = client.describe_security_groups()
        for index, securityGroup in enumerate(response["SecurityGroups"]):
            SecurityGroupIds.append(response["SecurityGroups"][index]["GroupId"])
            SecurityGroupNames.append(response["SecurityGroups"][index]["GroupName"])
            SecurityVpcIds.append(response["SecurityGroups"][index]["VpcId"])
        tab = tt.Texttable(max_width=120)
        headings = ['GroupName', 'GroupId', 'VpcId']
        tab.header(headings)
        for row in tuple(zip(SecurityGroupNames, SecurityGroupIds, SecurityVpcIds)):
            # print(row)
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
# ToDo Ubuntu/Amazon AMI - identify platform.
# ToDo Need to improve error handling.
def amis(profile, region):
    """list AMIs in current region"""
    ami_name_list = []
    ami_state_list = []
    ami_date_list = []
    ami_public_list = []
    ami_os_list = []
    ami_ena_support_list = []
    ami_sriovnet_list = []
    ami_hardware_list = []
    ami_region_list = []

    def common():
        boto3.setup_default_session(profile_name=profile, region_name=region)
        client = boto3.client('ec2')
        response = client.describe_images(
            Owners=[
                'self',
            ]
        )
        for index, _ami in enumerate(response['Images']):
            ami_name_list.append(response['Images'][index]['Name'])
            ami_state_list.append(response['Images'][index]['State'])
            ami_date_list.append(response['Images'][index]['CreationDate'])
            if response['Images'][index]['Public'] == 0:
                ami_public_list.append('False')
            else:
                ami_public_list.append('True')
            if response['Images'][index].get('PlatformDetails') is None:
                ami_os_list.append('Linux')
            else:
                ami_os_list.append(response['Images'][index]['PlatformDetails'])
            if response['Images'][index]['EnaSupport'] == 0:
                ami_ena_support_list.append('False')
            else:
                ami_ena_support_list.append('True')
            if response['Images'][index]['SriovNetSupport'] == 'simple':
                ami_sriovnet_list.append('True')
            else:
                ami_sriovnet_list.append('False')
            ami_hardware_list.append(response['Images'][index]['VirtualizationType'])
            ami_region_list.append(region)

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
        common()
    else:
        try:
            common()
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)

    tab = tt.Texttable(max_width=180)
    headings = ['Name', 'State', 'CreationDate', 'OS', 'Public', 'ENA-Support', 'SRIOVNet-Support',
                'Virtualization', 'Region']
    tab.header(headings)
    for row in tuple(
            zip(ami_name_list, ami_state_list, ami_date_list, ami_os_list, ami_public_list, ami_ena_support_list,
                ami_sriovnet_list, ami_hardware_list, ami_region_list)):
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)

    click.echo(click.style('Total AMIs: ' + str(len(ami_name_list)), fg='green', blink=True, bold=True))


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
def key_pairs(profile, region):
    """list EC2 key pairs in current region"""
    key_pair_name_list = []
    key_pair_region_list = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_key_pairs()
        for index, _key_pair in enumerate(response['KeyPairs']):
            key_pair_name_list.append(response['KeyPairs'][index]['KeyName'])
            key_pair_region_list.append(region)

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
        common()
    try:
        boto3.setup_default_session(profile_name=profile, region_name=region)
        common()
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)

    tab = tt.Texttable(max_width=120)
    headings = ['KeyName', 'Region']
    tab.header(headings)
    for row in tuple(
            zip(key_pair_name_list, key_pair_region_list)):
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


# @list.command()
# @click.option('--profile', required=False, type=str)
# def elastic_network_interfaces(profile):
#     """list ENIs in current region"""
#     boto3.setup_default_session(profile_name=profile)
#
#
# @list.command()
# @click.option('--profile', required=False, type=str)
# def load_balancers(profile):
#     """list EC2 load balancers in current region"""
#     boto3.setup_default_session(profile_name=profile)
#
#
# @list.command()
# @click.option('--profile', required=False, type=str)
# def load_balancer_target_groups(profile):
#     """list Target groups for Load Balancers in current region"""
#     boto3.setup_default_session(profile_name=profile)


# @list.command()
# def launch_configurations():
#     """list EC2 launch configurations in current region"""
#     pass
#
#
# @list.command()
# def auto_scaling_groups():
#     """list EC2 auto scaling groups in current region"""
#     pass


"""Describe Commands"""


@describe.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
@click.option('--sg-id', required=True, type=str)
# ToDo improve error handling
# ToDo introduce profile not found error exception

def security_group(profile, region, sg_id):
    """Describe a security group details"""
    click.echo(click.style('Ingress Rules', fg='green', blink=True, bold=True))

    ingress_from_port_list = []
    ingress_to_port_list = []
    ingress_protocols_list = []
    ingress_cidr_ranges_list = []
    boto3.setup_default_session(profile_name=profile, region_name=region)
    client = boto3.client('ec2')
    response = client.describe_security_groups(
        GroupIds=[
            sg_id,
        ]
    )
    ingress_rules = response['SecurityGroups'][0]['IpPermissions']
    for ingress_rule in ingress_rules:
        ip_range_exists = len(ingress_rule['IpRanges'])
        if ingress_rule.get('FromPort') is not None:
            ingress_from_port_list.append(ingress_rule['FromPort'])
            ingress_to_port_list.append(ingress_rule['ToPort'])
        else:
            ingress_from_port_list.append('All')
            ingress_to_port_list.append('All')
        if ip_range_exists:
            ingress_cidr_ranges_list.append(ingress_rule['IpRanges'])
            ingress_protocols_list.append(ingress_rule['IpProtocol'])
        else:
            ingress_protocols_list.append(ingress_rule['IpProtocol'])
            ingress_cidr_ranges_list.append(
                ingress_rule['UserIdGroupPairs'][0]['UserId'] + '/' + ingress_rule['UserIdGroupPairs'][0]['GroupId'])
    ingress_tab = tt.Texttable(max_width=100)
    headings = ['FromPort', 'ToPort', 'Protocol', 'Source']
    ingress_tab.header(headings)
    for row in tuple(
            zip(ingress_from_port_list, ingress_to_port_list, ingress_protocols_list, ingress_cidr_ranges_list)):
        ingress_tab.add_row(row)
    s = ingress_tab.draw()
    click.echo(s)

    click.echo(click.style('Egress Rules', fg='green', blink=True, bold=True))
    """Egress Rules"""

    egress_from_port_list = []
    egress_to_port_list = []
    egress_protocols_list = []
    egress_cidr_ranges_list = []
    egress_rules = response['SecurityGroups'][0]['IpPermissionsEgress']
    for egress_rule in egress_rules:
        ip_range_exists = len(egress_rule['IpRanges'])
        if egress_rule.get('FromPort') is not None:
            egress_from_port_list.append(egress_rule['FromPort'])
            egress_to_port_list.append(egress_rule['ToPort'])
        else:
            egress_from_port_list.append('All')
            egress_to_port_list.append('All')
        if ip_range_exists:
            egress_cidr_ranges_list.append(egress_rule['IpRanges'])
            egress_protocols_list.append(egress_rule['IpProtocol'])
        else:
            egress_protocols_list.append(egress_rule['IpProtocol'])
            egress_cidr_ranges_list.append(
                egress_rule['UserIdGroupPairs'][0]['UserId'] + '/' + egress_rule['UserIdGroupPairs'][0]['GroupId'])
    egress_tab = tt.Texttable(max_width=100)
    headings = ['FromPort', 'ToPort', 'Protocol', 'Source']
    egress_tab.header(headings)
    for row in tuple(zip(egress_from_port_list, egress_to_port_list, egress_protocols_list, egress_cidr_ranges_list)):
        egress_tab.add_row(row)
    s = egress_tab.draw()
    click.echo(s)


# ---------------------------------------------- IAM SubGroup ----------------------------------------------


@aws.group()
def iam():
    """Manage AWS IAM resources"""
    pass


@iam.group()
def list():
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
def users(profile):
    try:
        boto3.setup_default_session(profile_name=profile)
        client = boto3.client('iam')
        response = client.list_users()
        userList = {value["UserName"]: value["Arn"]
                    for value in response.get('Users')}
        userList = userList.items()
        tab = tt.Texttable(max_width=180)
        headings = ['UserName', 'Arn']
        tab.header(headings)
        for row in userList:
            tab.add_row(row)
        s = tab.draw()
        print(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
def groups(profile):
    try:
        boto3.setup_default_session(profile_name=profile)
        client = boto3.client('iam')
        response = client.list_groups()
        GroupList = {value["GroupName"]: value["Arn"]
                     for value in response.get('Groups')}
        GroupList = GroupList.items()
        tab = tt.Texttable(max_width=180)
        headings = ['GroupName', 'Arn']
        tab.header(headings)
        for row in GroupList:
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
def roles(profile):
    try:
        boto3.setup_default_session(profile_name=profile)
        client = boto3.client('iam')
        response = client.list_roles()
        RolesList = {value["RoleName"]: value["Arn"] for value in response.get('Roles')}
        RolesList = RolesList.items()
        tab = tt.Texttable(max_width=150)
        headings = ['RoleName', 'Arn']
        tab.header(headings)
        for row in RolesList:
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


# ---------------------------------------------- S3 SubGroup ----------------------------------------------


@aws.group()
def s3():
    """Manage AWS S3 resources"""
    pass


@s3.group()
def list():
    """Print the resources information"""
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
def buckets(profile):
    """list S3 buckets in current region"""
    try:
        boto3.setup_default_session(profile_name=profile)
        client = boto3.client('s3')
        response = client.list_buckets()
        bucket_name_list = []
        bucket_creation_date_list = []
        client = boto3.client('s3')
        response = client.list_buckets()
        for index, _bucket in enumerate(response['Buckets']):
            bucket_name_list.append(response['Buckets'][index]['Name'])
            bucket_creation_date_list.append((response['Buckets'][index]['CreationDate']))

        tab = tt.Texttable(max_width=150)
        headings = ['BucketName', 'CreationDate']
        tab.header(headings)
        for row in tuple(zip(bucket_name_list, bucket_creation_date_list)):
            # print(row)
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
def buckets_size_in_mb(profile):
    """list S3 bucket size in MB for current region"""
    try:
        boto3.setup_default_session(profile_name=profile)
        bucket_name_list = []
        bucket_size_list = []

        now = datetime.datetime.now()

        cw = boto3.client('cloudwatch')
        s3client = boto3.client('s3')

        # Get a list of all buckets
        allbuckets = s3client.list_buckets()

        # Iterate through each bucket
        for bucket in allbuckets['Buckets']:
            # For each bucket item, look up the cooresponding metrics from CloudWatch
            response = cw.get_metric_statistics(Namespace='AWS/S3',
                                                MetricName='BucketSizeBytes',
                                                Dimensions=[
                                                    {'Name': 'BucketName', 'Value': bucket['Name']},
                                                    {'Name': 'StorageType', 'Value': 'StandardStorage'}
                                                ],
                                                Statistics=['Average'],
                                                Period=3600,
                                                StartTime=(now - datetime.timedelta(days=1)).isoformat(),
                                                EndTime=now.isoformat()
                                                )
            # The cloudwatch metrics will have the single datapoint, so we just report on it.
            for item in response["Datapoints"]:
                bucket_name_list.append(bucket["Name"])
                bucket_size_list.append(int(item["Average"]) / 1024 / 1024)

        tab = tt.Texttable(max_width=180)
        headings = ['BucketName', 'BucketSizeInMB']
        tab.header(headings)
        for row in tuple(zip(bucket_name_list, bucket_size_list)):
            # print(row)
            tab.add_row(row)
        s = tab.draw()
        click.echo(s)
    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)


# ---------------------------------------------- SSM SubGroup ----------------------------------------------


@aws.group()
def ssm():
    """Manage AWS SSM resources"""
    pass


@ssm.group()
def list():
    """Print the resources information"""
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
# ToDo Need to add search functionality for ssm parameters

def parameters(profile, region):
    """list SSM Parameters in a requested region"""
    parameter_name_list = []
    parameter_value_list = []
    parameter_last_modified_date_list = []
    parameter_last_modified_user_list = []
    parameter_version_list = []
    parameter_region_list = []

    def common():
        ssm_client = boto3.client('ssm')
        response = ssm_client.describe_parameters()
        paginator = ssm_client.get_paginator('describe_parameters')
        response_iterator = paginator.paginate(
            PaginationConfig={
                'MaxItems': 999,
                'PageSize': 50,
            }
        )
        result = response_iterator.build_full_result()

        for index, _parameter in enumerate(result['Parameters']):
            parameter_last_modified_user_list.append(_parameter['LastModifiedUser'])
            parameter_details = ssm_client.get_parameters(
                Names=[
                    _parameter['Name']
                ],
                WithDecryption=True)
            parameter_name_list.append(parameter_details['Parameters'][0]['Name'])
            parameter_value_list.append(parameter_details['Parameters'][0]['Value'])
            parameter_version_list.append(parameter_details['Parameters'][0]['Version'])
            parameter_last_modified_date_list.append(parameter_details['Parameters'][0]['LastModifiedDate'])
            parameter_region_list.append(region)

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
            ssm_client = boto3.client('ssm')
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)

    tab = tt.Texttable(max_width=180)
    headings = ['ParameterName', 'ParameterValue', 'Version', 'LastModifiedUser', 'LastModifiedDate', 'Region']
    tab.header(headings)
    for row in tuple(
            zip(parameter_name_list, parameter_value_list, parameter_version_list, parameter_last_modified_user_list,
                parameter_last_modified_date_list, parameter_region_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


# ---------------------------------------------- VPC SubGroup ----------------------------------------------


@aws.group()
def vpc():
    """Manage AWS vpc resources"""
    pass


@vpc.group()
def list():
    """Prints AWS vpc resources information"""
    pass


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
def vpcs(profile, region):
    """List all the VPCs in current region"""
    vpcIds = []
    vpcStates = []
    vpcCidrs = []
    vpcDefaults = []
    vpcRegions = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_vpcs()
        vpcInfo = response['Vpcs']
        for index, vpcId in enumerate(vpcInfo):
            vpcIds.append(vpcInfo[index]['VpcId'])
            vpcStates.append(vpcInfo[index]['State'])
            vpcCidrs.append(vpcInfo[index]['CidrBlock'])
            vpcDefaults.append(vpcInfo[index]['IsDefault'])
            vpcRegions.append(region)

    try:
        boto3.setup_default_session(profile_name=profile, region_name=region)
        common()

    except botocore.exceptions.ProfileNotFound:
        click.echo(
            click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                        f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
        sys.exit(1)

    tab = tt.Texttable(max_width=180)
    headings = ['VpcId', 'State', 'CidrRange', 'IsDefault', 'Region']
    tab.header(headings)
    for row in tuple(zip(vpcIds, vpcStates, vpcCidrs, vpcDefaults, vpcRegions)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
def detached_elastic_ips(profile, region):
    """list all unattached EIPs in current region"""
    unattached_elastic_ip_list = []
    unattached_elastic_ip_allocation_id_list = []
    unattached_elastic_ip_region_id_list = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_addresses()
        if response['Addresses']:
            for index, _address in enumerate(response['Addresses']):
                if response['Addresses'][index].get('AssociationId') is None:
                    unattached_elastic_ip_list.append(response['Addresses'][index]['PublicIp'])
                    unattached_elastic_ip_allocation_id_list.append(response['Addresses'][index]['AllocationId'])
                    unattached_elastic_ip_region_id_list.append(region)
                else:
                    pass
                    # click.echo(click.style('All the EIPs are attached', fg='green', blink=True, bold=True)
        else:
            pass
            # click.echo(click.style(f'No EIPs allocated in : {region}', fg='green', blink=True, bold=True))

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)

    tab = tt.Texttable(max_width=180)
    headings = ['Elastic-IP', 'EIP-Allocation-ID', 'Region']
    tab.header(headings)
    for row in tuple(zip(unattached_elastic_ip_list, unattached_elastic_ip_allocation_id_list,
                         unattached_elastic_ip_region_id_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
def nat_gateways(profile, region):
    """list all NAT gateways in current region"""
    nat_gateway_addresses_list = []
    nat_gateway_state_list = []
    nat_gateway_vpc_list = []
    nat_gateway_public_ip_list = []
    nat_gateway_create_time_list = []
    nat_gateway_region_list = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_nat_gateways()

        if not response['NatGateways']:
            pass
        else:
            for index, _nat_gateway in enumerate(response['NatGateways']):
                nat_gateway_addresses_list.append(response['NatGateways'][index]['NatGatewayId'])
                nat_gateway_state_list.append(response['NatGateways'][index]['State'])
                nat_gateway_vpc_list.append(response['NatGateways'][index]['VpcId'])
                nat_gateway_create_time_list.append(response['NatGateways'][index]['CreateTime'])
                nat_gateway_region_list.append(region)
                for index2, _nat_gateway_addresses in enumerate(response['NatGateways'][index]['NatGatewayAddresses']):
                    if response['NatGateways'][index]['NatGatewayAddresses'][index2].get('PublicIp') is None:
                        nat_gateway_public_ip_list.append('Not Available')
                    else:
                        nat_gateway_public_ip_list.append(response['NatGateways'][index]['NatGatewayAddresses'][index2]
                                                          ['PublicIp'])

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)

    tab = tt.Texttable(max_width=120)
    headings = ['NATGatewayId', 'State', 'VpcId', 'PublicIp', 'CreateTime', 'Region']
    tab.header(headings)
    for row in tuple(zip(nat_gateway_addresses_list, nat_gateway_state_list, nat_gateway_vpc_list,
                         nat_gateway_public_ip_list, nat_gateway_create_time_list, nat_gateway_region_list)):
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)


@list.command()
@click.option('--profile', required=False, show_default=True, default='default', type=str,
              help='Enter AWS profile name')
@click.option('--region', required=False, show_default=True, default='eu-west-1', type=str,
              help='Enter AWS region name')
def internet_gateways(profile, region):
    """list all Internet gateways in current region"""
    igw_id_list = []
    igw_vpc_attachment_list = []
    igw_vpc_region_list = []

    def common():
        client = boto3.client('ec2')
        response = client.describe_internet_gateways()
        for index, _igw_attachment in enumerate(response['InternetGateways']):
            igw_id_list.append(response['InternetGateways'][index]['InternetGatewayId'])
            igw_vpc_attachment_list.append((response['InternetGateways'][index]['Attachments'][0]['VpcId']))
            igw_vpc_region_list.append(region)

    if region == 'all':
        client = boto3.client('ec2', region_name='us-east-1')
        ec2_regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
        for region in ec2_regions:
            try:
                boto3.setup_default_session(profile_name=profile, region_name=region)
                common()
            except botocore.exceptions.ProfileNotFound:
                click.echo(
                    click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                                f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
                sys.exit(1)
    else:
        try:
            boto3.setup_default_session(profile_name=profile, region_name=region)
            common()
        except botocore.exceptions.ProfileNotFound:
            click.echo(
                click.style(f"kloudy could not find AWS Profile named {profile} in $HOME/.aws/credentials file. "
                            f"Please check your AWS profile configuration.", fg='red', blink=True, bold=True))
            sys.exit(1)

    tab = tt.Texttable(max_width=120)
    headings = ['IgwId', 'VpcId', 'Region']
    tab.header(headings)
    for row in tuple(zip(igw_id_list, igw_vpc_attachment_list, igw_vpc_region_list)):
        # print(row)
        tab.add_row(row)
    s = tab.draw()
    click.echo(s)
