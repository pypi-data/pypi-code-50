import unittest

from unittest import TestCase, mock

from aws.ec2 import *
from aws.region import *
from aws.cfm import *
from aws.elb import *
from aws.rds import *

from po.pretty_object import PrettyObject
import pprint

po = PrettyObject()
pp = pprint.PrettyPrinter(indent=2, width=40)


def abs_path(file: str):
    """
    Sets an absolute path relative to the **k9** package directory.

    Example::
        result = abs_path('myfile)

    Result::
        /Users/simon/git/k9/k9/myfile


    This is used primarily for building unit tests within the K9 package
    and is not expected to be useful to K9 library users.

    :param file: File or directory to attach absolute path with
    :return: absolute path to specified file or directory
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(basedir, file)


class TestConfiguration(TestCase):

    def test_aaa(self):
        try:
            # Create the stack to test against
            stack1_name = 'unit-00-rancher-vpc'
            stack2_name = 'unit-01-rancher-bastion'
            stack3_name = 'unit-02-rancher-rds'
            key_name = 'unit-key_pair'
            kp = create_key_pair(key_name)

            parameters = {
                'EnvType': 'unit',
                'CidrPrefix': '10.222',
                'DomainName': 'unit.simoncomputing.com',
                'KeyName': key_name,
                'azs': list_azs()
            }

            # Test create_stack
            stack = create_stack(abs_path('00-rancher-vpc.yaml'), parameters, debug=False)
            self.assertTrue(stack_exists(stack1_name))

            # Test second try without failure
            stack = create_stack(abs_path('00-rancher-vpc.yaml'), parameters)

            stack = create_stack(abs_path('01-rancher-bastion.yaml'), {'EnvType': 'unit'})
            self.assertTrue(stack_exists(stack2_name))

            # Test three
            stack = create_stack(abs_path('02-rancher-rds.yaml'), {'EnvType': 'unit'})

            # Test get_stack()
            stack = get_stack(stack1_name)
            self.assertIsNotNone(stack)



        finally:
            # If you are testing something repeatedly, you could comment the
            # delete statements out so that you don't have to re-create the
            # stacks to perform your testing.  The create actions will not
            # execute if the keypairs and stacks already exist.

            delete_key_pair(key_name)
            # delete_stack(stack2_name)
            # delete_stack(stack1_name)
            pass


    def test_get_regions(self):
        region = 'us-east-1'
        set_default_region(region)
        regions = list_regions()
        found = [
            region['RegionName']
            for region in regions
            if region['RegionName'] == 'us-east-1'
        ]
        self.assertEqual(1, len(found))

    def test_list_azs(self):
        azs = list_azs()
        found = [
            az['ZoneName']
            for az in azs
            if az['ZoneName'] == 'us-east-1a'
        ]
        self.assertEqual(1, len(found))

    def test_default_region(self):
        region = 'us-east-1'
        set_default_region(region)
        self.assertEqual(region, get_default_region())


    ###########################################################################
    # VPC
    ###########################################################################

    def test_default_vpc(self):

        vpc = get_vpc(name='unit-rancher-vpc')
        self.assertIsNotNone(vpc)

        vpcid = get_vpcid(vpc)
        self.assertIsNotNone(vpcid)

        set_current_vpcid(vpc)
        self.assertEqual(vpcid, get_current_vpcid())

        set_current_vpcid()
        set_current_vpcid(vpc)
        self.assertEqual(vpcid, get_current_vpcid())

        set_current_vpcid()
        set_current_vpcid(vpcid=vpcid)
        self.assertEqual(vpcid, get_current_vpcid())

    def test_list_vpcs(self):
        # List just the default
        vpc = get_vpc(default=True)
        self.assertIsNotNone(vpc)
        self.assertTrue(vpc['IsDefault'])
        vpcids = [vpc.get('VpcId')]

        # List by name

        vpc = get_vpc(name="unit-rancher-vpc")
        self.assertIsNotNone(vpc)
        vpcids.append(vpc.get('VpcId'))

        vpc = get_vpc(vpcid=get_vpcid(vpc))
        self.assertIsNotNone(vpc)
        self.assertTrue('unit-rancher-vpc', get_tag_value(vpc, 'Name'))

        # List all
        vpcs = list_vpcs()
        self.assertTrue(len(vpcs) > 0)
        found = [
            vpc
            for vpc in vpcs
            if vpc.get('VpcId') in vpcids
        ]
        self.assertEqual(2, len(found))

    def test_vpc_failures(self):
        result = get_vpc(vpcid='bogus')
        self.assertIsNone(result)

        set_current_vpcid(None)
        with self.assertRaisesRegex(Exception, 'You must call set_current_vpc()'):
            get_current_vpcid()

        with self.assertRaisesRegex(Exception, 'You must call set_current_vpc()'):
            get_vpc_filter()

        with self.assertRaisesRegex(Exception, 'default, name or vpcid must be provided when calling get_vpc()'):
            get_vpc()

    ###########################################################################
    # Subnets
    ###########################################################################

    def test_list_subnets(self):
        set_current_vpcid(get_vpc(name="unit-rancher-vpc"))
        vpcid = get_current_vpcid()

        for subnet in list_subnets():
            self.assertEqual(vpcid, get_vpcid(subnet))

        # Call with subnet_type
        subnets = list_subnets(subnet_type='private')
        for subnet in subnets:
            self.assertEqual('private', get_tag_value(subnet, 'SubnetType'))

        # Call with filter
        subnets = list_subnets({'SubnetType': 'public'})
        for subnet in subnets:
            self.assertEqual('public', get_tag_value(subnet, 'SubnetType'))

        subnet_id = get_subnet_id(subnets[0])
        subnet = get_subnet(subnet_id)
        self.assertEqual(subnet_id, get_subnet_id(subnet))

    def test_get_subnet(self):
        set_current_vpcid(get_vpc(default=True))

        subnet = get_subnet("bogus")
        self.assertIsNone(subnet)

    ###########################################################################
    # Internet Gateways & NATs
    ###########################################################################
    def test_list_igws(self):
        set_current_vpcid(vpc = get_vpc(name='unit-rancher-vpc'))
        igws = list_igws()
        self.assertIsNotNone(igws)

        igw = get_vpc_igw()
        self.assertIsNotNone(igw)
        self.assertEqual(get_current_vpcid(), igw['Attachments'][0]['VpcId'])

    def test_list_nats(self):
        set_current_vpcid(vpc = get_vpc(name='unit-rancher-vpc'))
        nats = list_nats()
        self.assertIsNotNone(nats)

        current_vpcid = get_current_vpcid()
        for nat in nats:
            self.assertEqual(current_vpcid, nat.get('VpcId'))

    def test_list_eips(self):
        eips = list_eips()
        self.assertIsNotNone(eips)

    ###########################################################################
    # Route Tables
    ###########################################################################

    def test_list_route_tables(self):
        set_current_vpcid(vpc = get_vpc(name='unit-rancher-vpc'))
        current_vpcid = get_current_vpcid()

        rts = list_route_tables()
        for rt in rts:
            self.assertEqual(current_vpcid, rt.get('VpcId'))

        name = 'unit-public-rt'
        criteria = {'Name': name}
        rts = list_route_tables(criteria)
        for rt in rts:
            self.assertTrue(name, get_tag_value(rt, 'Name'))

    def test_get_route_table(self):
        set_current_vpcid(vpc = get_vpc(name='unit-rancher-vpc'))
        name = 'unit-public-rt'
        rt = get_route_table(name)
        self.assertIsNotNone(name)
        self.assertEqual(name, get_tag_value(rt, 'Name'))

        rt_id = get_route_table_id(rt)

        rt = get_route_table(rt_id=rt_id)
        self.assertIsNotNone(name)
        self.assertEqual(name, get_tag_value(rt, 'Name'))

        subnets = list_subnets(subnet_type='public')
        subnet_id = get_subnet_id(subnets[0])

        rt = get_route_table(subnet_id=subnet_id)
        self.assertIsNotNone(rt)
        self.assertEqual(name, get_tag_value(rt, 'Name'))

        subnets = list_subnets(subnet_type='private')
        subnet_id = get_subnet_id(subnets[0])

        rt = get_route_table(subnet_id=subnet_id)
        self.assertIsNotNone(45)
        self.assertEqual('unit-private-rt', get_tag_value(rt, 'Name'))

    def test_get_route_table_fail(self):
        set_current_vpcid(vpc = get_vpc(name='unit-rancher-vpc'))

        rt = get_route_table(name='bogus')
        self.assertIsNone(rt)

        rt = get_route_table(rt_id='bogus')
        self.assertIsNone(rt)

        rt = get_route_table(subnet_id='bogus')
        self.assertIsNone(rt)

        with self.assertRaisesRegex(Exception, 'name, rt_id or subnet_id must be specified'):
            get_route_table()

    ###########################################################################
    # Security Groups
    ###########################################################################

    def test_security_groups(self):
        set_current_vpcid(get_vpc(name='unit-rancher-vpc'))
        sgs = list_sgs({'Name': 'unit-https-all-sg'})
        self.assertEqual(1, len(sgs))
        self.assertEqual('unit-https-all-sg', get_tag_value(sgs[0], 'Name'))

        sgs = list_sgs({'Name': 'unit-https-all-sg'})

        sg = get_sg(name='unit-https-all-sg')
        self.assertIsNotNone(sg)
        self.assertEqual('unit-https-all-sg', get_tag_value(sg, 'Name'))
        sgid = get_sgid(sg)

        sg = get_sg(sgid=sgid)
        self.assertIsNotNone(sg)
        self.assertEqual('unit-https-all-sg', get_tag_value(sg, 'Name'))

    def test_get_security_group_fail(self):
        set_current_vpcid(get_vpc(default=True))

        sg = get_sg(name="bogus")
        self.assertIsNone(sg)

        sgid = get_sgid({})
        self.assertIsNone(sgid)

        with self.assertRaisesRegex(Exception, 'You must provide name or sgid'):
            get_sg()

    ###########################################################################
    # Tags
    ###########################################################################
    def test_get_ec2_tags(self):
        vpc = {
            'CidrBlock': '172.31.0.0/16',
            'CidrBlockAssociationSet': [
                {
                    'AssociationId': 'vpc-cidr-assoc-d27fffbe',
                    'CidrBlock': '172.31.0.0/16',
                    'CidrBlockState': {
                        'State': 'associated'
                    }
                }
            ],
            'DhcpOptionsId': 'dopt-905f0feb',
            'InstanceTenancy': 'default',
            'IsDefault': True,
            'OwnerId': '862586795542',
            'State': 'available',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'default-vpc'
                }
            ],
            'VpcId': 'vpc-b43582ce'
        }

        tags = get_ec2_tags(vpc)
        self.assertEqual('default-vpc', tags['Name'])

    def test_get_tag_fail(self):
        result = get_tag_value({'Tags': [{'Key': 'Name', 'Value': 'default-vpc'}]}, 'Namex')
        self.assertIsNone(result)

    def test_match_tags(self):
        vpc = {
            'InstanceTenancy': 'default',
            'IsDefault': True,
            'State': 'available',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'default-vpc'
                },
                {
                    'Key': 'EnvType',
                    'Value': 'dev'
                }
            ],
            'VpcId': 'vpc-b43582ce'
        }

        self.assertTrue(match_tags({'Name': 'default-vpc'}, vpc))
        self.assertFalse(match_tags({'Name': 'bogus'}, vpc))
        self.assertTrue(match_tags({'Name': 'default-vpc', 'EnvType': 'dev'}, vpc))
        self.assertFalse(match_tags({'Name': 'default-vpc', 'EnvType': 'test'}, vpc))
        self.assertFalse(match_tags({'Name': 'bogus'}, {}))

    def test_set_tag_no_instance(self):
        set_current_vpcid(get_vpc(default=True))
        self.assertIsNone(set_tag(name = 'bogus_not_a_name', key = 'asdf', value = 'jkl'))
        self.assertIsNone(set_tag(key = 'asdf', value = 'jkl'))

    def test_set_tag_success(self):
        set_current_vpcid(get_vpc(default=True))
        try:
            create_stack(abs_path('unit-basic-stack.yaml'), stack_name='unit-set-tag-success')
            self.assertIsNotNone(set_tag(name = 'unit-test-basic-instance', key = 'asdf', value = 'jkl'))
            self.assertEqual(get_tag_value(aws_obj = get_instance(name = 'unit-test-basic-instance'), key = 'asdf'), 'jkl')
        finally:
            delete_stack('unit-set-tag-success')

    def test_ready_none(self):
        set_current_vpcid(get_vpc(default=True))
        self.assertIsNone(wait_for_ready(name = 'bogus_not_a_name'))
        self.assertIsNone(wait_for_ready(instance_id = 'i12345678'))

    def test_not_ready(self):
        set_current_vpcid(get_vpc(default=True))
        try:
            create_stack(abs_path('unit-basic-stack.yaml'), stack_name='unit-not-ready')
            self.assertFalse(wait_for_ready(name = 'unit-test-basic-instance', interval = 5, timeout = 10))
        finally:
            delete_stack('unit-not-ready')
    
    def test_ready(self):
        set_current_vpcid(get_vpc(default=True))
        try:
            create_stack(abs_path('unit-basic-stack.yaml'), stack_name='unit-ready-asap')
            set_tag(name = 'unit-test-basic-instance', key = 'Ready', value = 'true')
            self.assertTrue(wait_for_ready(name = 'unit-test-basic-instance', interval = 5, timeout = 15))
        finally:
            delete_stack('unit-ready-asap')
    ###########################################################################
    # KeyPairs
    ###########################################################################

    def test_key_pairs(self):
        try:
            # Test create_key_pair()
            name = "unit-kp"
            kp = create_key_pair(name)
            self.assertEqual(name, kp.get('KeyName'))

            # Test key_pair_exists()
            self.assertTrue(key_pair_exists(name))

            # Test list_key_pairs()
            kps = list_key_pairs()
            found = [
                kp
                for kp in kps
                if kp.get('KeyName') == name
            ]
            self.assertEqual(1, len(found))
            self.assertEqual(name, found[0].get('KeyName'))

            # Test delete_key_pair()
            delete_key_pair(name)
            self.assertFalse(key_pair_exists(name))

        finally:
            delete_key_pair(name)

    def test_wait_on_key_pairs(self):
        try:
            self.assertFalse(wait_for_key_pair(name = 'test_key_pair_1234', interval = 5, timeout = 10))
            create_key_pair('test_key_pair_1234')
            self.assertTrue(wait_for_key_pair(name = 'test_key_pair_1234', interval = 5, timeout = 10))
            self.assertFalse(wait_for_key_pair(name = 'asdfjkl', interval = 5, timeout = 10))
        finally:
            delete_key_pair('test_key_pair_1234')

    ###########################################################################
    # AMIs
    ###########################################################################
    def test_get_linux2_ami(self):
        imageid = get_linux2_ami()
        self.assertIsNotNone(imageid)

        response = get_image(imageid)
        self.assertIsNotNone(response)

    ###########################################################################
    # EC2 Instances
    ###########################################################################

    def test_list_get_instances(self):
        set_current_vpcid(vpc = get_vpc(name='unit-rancher-vpc'))
        # Test list_instance()
        instances = list_instances()
        self.assertTrue(len(instances) > 0)

        # Test list_instance(search_filter)
        name = 'unit-bastion'
        instances = list_instances({'Name': name})
        self.assertEqual(1, len(instances))
        self.assertEqual(name, get_tag_value(instances[0], 'Name'))

        # Test get_instance(name)
        instance = get_instance(name)
        self.assertIsNotNone(instance)
        self.assertEqual(name, get_tag_value(instance, 'Name'))

        instance = get_instance(name=name)
        self.assertIsNotNone(instance)
        self.assertEqual(name, get_tag_value(instance, 'Name'))

        # Test get_instance(instance_id)
        instance_id = get_instance_id(instances[0])
        instance = get_instance(instance_id=instance_id)
        self.assertIsNotNone(instance)
        self.assertEqual(name, get_tag_value(instance, 'Name'))

    def test_get_instance_fail(self):
        set_current_vpcid(get_vpc(default=True))

        instance = get_instance('bogus')
        self.assertIsNone(instance)

        instance = get_instance(name='bogus')
        self.assertIsNone(instance)

        instance = get_instance(instance_id='bogus')
        self.assertIsNone(instance)

        with self.assertRaisesRegex(Exception, 'name or instance_id must be provided'):
            get_instance()

    ###########################################################################
    # SSM
    ###########################################################################

    def test_ssm_run_shell_script(self):
        set_current_vpcid(get_vpc(default=True))
        try:
            create_stack(abs_path('unit-basic-ssm.yaml'), stack_name='unit-run-shell-script', capabilities=['CAPABILITY_NAMED_IAM'])
            wait_for_ready(name = 'unit-test-ssm-instance', timeout = 240)
            commands = ['echo hello', 'echo world']
            response = ssm_run_shell_script(name = 'unit-test-ssm-instance', commands = commands, comment = 'test run shell script')
            self.assertIsNotNone(response)
            self.assertEqual('test run shell script', response['Command']['Comment'])
        finally:
            delete_stack('unit-run-shell-script')
    ###########################################################################
    # Classic Load Balancer
    ###########################################################################

    def test_list_classic_loadbalancer(self):
        elbs = list_classic_loadbalancer()
        found = [
            elb['LoadBalancerName']
            for elb in elbs
            if elb['LoadBalancerName'] == 'unit-classic-loadbalancer'
        ]
        self.assertEqual(1, len(found))

    def test_get_classic_loadbalancer_fail(self):
        elb = get_classic_loadbalancer("null")
        self.assertIsNone(elb)

    def test_get_classic_loadbalancer(self):
        elb = get_classic_loadbalancer('unit-classic-loadbalancer')
        self.assertIsNotNone(elb)

    ###########################################################################
    # Application Load Balancer
    ###########################################################################

    def test_list_application_loadbalancer(self):
        elbv2s = list_application_loadbalancer()
        found = [
            elbv2['LoadBalancerName']
            for elbv2 in elbv2s
            if elbv2['LoadBalancerName'] == 'unit-load-balancer'
        ]
        self.assertEqual(1, len(found))

    def test_get_application_loadbalancer(self):
        elbv2 = get_application_loadbalancer(name='unit-load-balancer')
        self.assertIsNotNone(elbv2)

    def test_get_application_loadbalancer_fail(self):
        elbv2 = get_application_loadbalancer('null')
        self.assertIsNone(elbv2)

    ###########################################################################
    # Target Groups
    ###########################################################################

    def test_list_target_groups(self):
        tgs = list_target_groups()
        found = [
            tg['TargetGroupName']
            for tg in tgs
            if tg['TargetGroupName'] == 'unit-worker-tg'
        ]
        self.assertEqual(1, len(found))

    def test_get_target_group(self):
        tg = get_target_group(name='unit-worker-tg')
        self.assertIsNotNone(tg)

    def test_get_target_group_fail(self):
        tg = get_target_group('null')
        self.assertIsNone(tg)

    def test_get_targets_in_group_empty(self):
        set_current_vpcid(get_vpc(name = 'unit-rancher-vpc'))
        tg = get_target_group(name = 'unit-worker-tg')
        self.assertIsNotNone(tg)
        empty = get_targets_in_group(group_name = 'unit-worker-tg')
        self.assertEqual([], empty)
        empty2 = get_targets_in_group(group_arn = tg['TargetGroupArn'])
        self.assertEqual([], empty2)
        self.assertFalse(get_targets_in_group())
        self.assertFalse(get_targets_in_group(group_name = 'asdf'))
        self.assertFalse(get_targets_in_group(group_arn = 'asdf'))


    def test_add_target(self):
        set_current_vpcid(get_vpc(name = 'unit-rancher-vpc'))
        tg = get_target_group(name='unit-worker-tg')
        self.assertIsNotNone(tg)
        target = get_instance('unit-bastion')
        self.assertIsNotNone(target)
        add_target(target_name = 'unit-bastion', group_name = 'unit-worker-tg')
        target_list = get_targets_in_group(group_name = 'unit-worker-tg')
        self.assertEquals(1, len(target_list))

    ###########################################################################
    # Database Clusters & Instances
    ###########################################################################

    def test_list_db_clusters(self):
        clusters = list_db_clusters()
        found = [
            cluster['DBClusterIdentifier']
            for cluster in clusters
            if cluster['DBClusterIdentifier'] == 'unit-cluster'
        ]
        self.assertEqual(1, len(found))

    def test_get_db_cluster(self):
        cluster = get_db_cluster('unit-cluster')
        self.assertIsNotNone(cluster)

    def test_get_db_cluster_fail(self):
        cluster = get_db_cluster('invalid-cluster')
        self.assertEqual(0, len(cluster))

    def test_set_deletion_protection_cluster(self):
        set_db_cluster_delete_protection('unit-cluster', True)
        try:
            delete_cluster('unit-cluster')
        except:
            pass

    def test_list_db_instances(self):
        instances = list_db_instances()
        found = [
            instance['DBInstanceIdentifier']
            for instance in instances
            if instance['DBInstanceIdentifier'] == 'unit-instance'
        ]
        self.assertEqual(1, len(found))

    def test_get_db_instance(self):
        instance = get_db_instance('unit-instance')
        self.assertIsNotNone(instance)

    def test_get_db_instance_fail(self):
        instance = get_db_instance('invalid-instance')
        self.assertEqual(0, len(instance))

    def test_set_deletion_protection_instance(self):
        try:
            set_db_instance_delete_protection('unit-instance', True)
            delete_instance('unit-instance')
        except:
            pass

    ###########################################################################
    # Database Subnet Groups
    ###########################################################################

    def test_list_subnet_groups(self):
        groups = list_subnet_groups()
        found = [
            group['DBSubnetGroupName']
            for group in groups
            if group['DBSubnetGroupName'] == 'unit-subnet-group'
        ]
        self.assertEqual(1, len(found))

    def test_get_subnet_group(self):
        set_current_vpcid(get_vpc(name="unit-rancher-vpc"))
        group = get_subnet_group('unit-subnet-group')
        self.assertIsNotNone(group)

    def test_get_subnet_group_fail(self):
        set_current_vpcid(get_vpc(name="unit-rancher-vpc"))
        try:
            get_subnet_group('invalid-subnet-group')
        except:
            pass
    ###########################################################################
    # Database Security Groups
    ###########################################################################

    def test_list_db_sgs(self):
        sec_groups = list_db_sgs()
        found = [
            sec_group['DBSecurityGroupName']
            for sec_group in sec_groups
            if sec_group['DBSecurityGroupName'] == 'default'
        ]
        self.assertEqual(1, len(found))

    def test_get_db_sg(self):
        sec_group = get_db_sg('default')
        self.assertIsNotNone(sec_group)


    def test_zzz(self):
        try:
            # Delete the stacks
            stack1_name = 'unit-00-rancher-vpc'
            stack2_name = 'unit-01-rancher-bastion'
            stack3_name = 'unit-02-rancher-rds'
            set_db_cluster_delete_protection('unit-cluster', False)
            #set_db_instance_delete_protection('unit-instance', False)
            delete_stack(stack3_name)
            delete_stack(stack2_name)
            delete_stack(stack1_name)

        finally:
            pass
