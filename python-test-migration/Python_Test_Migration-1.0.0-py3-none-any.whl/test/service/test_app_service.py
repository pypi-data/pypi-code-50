from unittest import TestCase
import sys
sys.path.append("..")
from service.app_service import *
from provider.constant import IP_ADDRESS


class Test(TestCase):
    def test_credentials_create(self):
        """Function to unit test Service Layer method test_credentials"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        creds1 = credentials_create(test_username,
                                    test_password,
                                    test_ipaddress)

        assert creds1.get_Credentials()['username'] == test_username
        assert creds1.get_Credentials()['password'] == test_password
        assert creds1.get_Credentials()['domain'] == test_ipaddress.get_ipaddress()

    def test_credentials_get(self):
        """Function to unit test Service Layer to get credentials"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        creds1 = credentials_create(test_username,
                                    test_password,
                                    test_ipaddress)

        result = credentials_get(creds1)

        assert result['username'] == test_username
        assert result['password'] == test_password
        assert result['domain'] == test_ipaddress.get_ipaddress()

    def test_mountpoint_create(self):
        """Function to unit test Service Layer to create mountpoint"""
        test_mountpoint_name = 'C:\\'
        test_mountpoint_size = 25
        mountpoint1 = mountpoint_create(test_mountpoint_name,
                                        test_mountpoint_size)

        print(mountpoint1.get_mountPoint_instances())

        assert mountpoint1.get_mountPoint_instances()['mount_name'] == test_mountpoint_name
        assert mountpoint1.get_mountPoint_instances()['size'] == test_mountpoint_size

    def test_mountpoint_get(self):
        """Function to unit test Service Layer to get mountpoint Details"""
        test_mountpoint_name = 'C:\\'
        test_mountpoint_size = 25
        mountpoint1 = mountpoint_create(test_mountpoint_name,
                                        test_mountpoint_size)

        result = mountpoint_get(mountpoint1)
        print(result)

        assert result['mount_name'] == test_mountpoint_name
        assert result['size'] == test_mountpoint_size

    def test_mountpoint_list(self):
        """Function to unit test Service Layer to get mountpoint list"""

        test_mountpoint1 = mountpoint_create('C:\\', 25)
        test_mountpoint2 = mountpoint_create('D:\\', 25)

        result = mountpoints_list(test_mountpoint1, test_mountpoint2)

        assert result[0] == test_mountpoint1.get_mountPoint_instances()
        assert result[1] == test_mountpoint2.get_mountPoint_instances()

    def test_workload_create(self):
        """Function to unit test Service Layer to create workload"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        creds1 = credentials_create(test_username,
                                    test_password,
                                    test_ipaddress)

        test_mountpoint1 = mountpoint_create('C:\\', 25)

        result = workload_create(creds1, test_mountpoint1.get_mountPoint_instances())

        assert result.get_workload()['username'] == test_username
        assert result.get_workload()['password'] == test_password
        assert result.get_workload()['domain'] == test_ipaddress.get_ipaddress()

    def test_workload_get(self):
        """Function to unit test Service Layer to get workload details"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        creds1 = credentials_create(test_username,
                                    test_password,
                                    test_ipaddress)

        test_mountpoint1 = mountpoint_create('C:\\', 25)
        test_workload = workload_create(creds1, test_mountpoint1.get_mountPoint_instances())
        result = workload_get(test_workload)

        assert result['username'] == test_username
        assert result['password'] == test_password
        assert result['domain'] == test_ipaddress.get_ipaddress()

    def test_check_constrains(self):
        """Function to unit test Service Layer to get workload details"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        creds1 = Credentials(test_username,
                             test_password,
                             test_ipaddress.get_ipaddress())

        test_mountpoint_name = 'C:\\'
        test_mountpoint_size = 25
        mountpoint1 = MountPoint(test_mountpoint_name, test_mountpoint_size)
        MountPoints_list = [mountpoint1.get_mountPoint_instances()]

        test_source = Workload(creds1, MountPoints_list)

        check_constrains = constrains(test_source, test_ipaddress)

        assert check_constrains['key'] == 'success'

    def test_check_constrains_IP_Changed(self):
        """Function to unit test class Workload constrains method when IP address changed in workload"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')
        changed_ip = '1.1.1.1'

        creds1 = Credentials(test_username,
                             test_password,
                             changed_ip)

        test_mountpoint_name = 'C:\\'
        test_mountpoint_size = 25
        mountpoint1 = MountPoint(test_mountpoint_name, test_mountpoint_size)
        MountPoints_list = [mountpoint1.get_mountPoint_instances()]

        test_source = Workload(creds1, MountPoints_list)
        check_constrains = constrains(test_source, test_ipaddress)

        assert check_constrains['key'] == 'error'

    def test_check_constrains_None_Parameters(self):
        """Function to unit test class Workload constrains method when None Parameters"""
        test_username = ""
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')
        changed_ip = '1.1.1.1'

        creds1 = Credentials(test_username, test_password, changed_ip)

        test_mountpoint_name = 'C:\\'
        test_mountpoint_size = 25
        mountpoint1 = MountPoint(test_mountpoint_name, test_mountpoint_size)
        MountPoints_list = [mountpoint1.get_mountPoint_instances()]

        test_source = Workload(creds1, MountPoints_list)
        check_constrains = constrains(test_source, test_ipaddress)

        assert check_constrains['key'] == 'error'

    def test_check_check_duplicate_ip(self):
        """Function to unit test Service Layer to check sources from duplicate IP addresses"""
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('1.1.1.1')
        sources = []

        creds1 = Credentials(test_username1,
                             test_password1,
                             test_ipaddress1.get_ipaddress())

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, MountPoints_list1)
        sources.append(test_source1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)
        sources.append(test_source2)

        result = check_duplicate_ip(sources)

        assert result['key'] == 'success'

    def test_check_check_duplicate_ip_ip_provided(self):
        """Function to unit test Service Layer to check sources from duplicate IP addresses
           Duplicate IP's provided in this case
        """
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('2.2.2.2')
        sources = []
        creds1 = Credentials(test_username1,
                             test_password1,
                             test_ipaddress1.get_ipaddress())

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, MountPoints_list1)
        sources.append(test_source1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)
        sources.append(test_source2)

        result = check_duplicate_ip(sources)

        assert result['key'] == 'error'

    def test_migrationTarget_Create(self):
        """Function to unit test Service Layer to create Migration target"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username,
                                       test_password,
                                       test_ipaddress.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        targetVM = migrationTarget_Create(test_cloud_type,
                                          test_creds_cloud,
                                          test_cloud_workload)

        assert targetVM.get_Migration_Target()['cloud_type'] == test_cloud_type
        assert targetVM.get_Migration_Target()['username'] == test_username
        assert targetVM.get_Migration_Target()['password'] == test_password
        assert targetVM.get_Migration_Target()['domain'] == test_ipaddress.get_ipaddress()
        assert targetVM.get_Migration_Target()['mountpoint'] == test_cloud_workload.storage

    def test_migrationTarget_get(self):
        """Function to unit test Service Layer to get Migration Target details"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username,
                                       test_password,
                                       test_ipaddress.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        targetVM = migrationTarget_Create(test_cloud_type,
                                          test_creds_cloud,
                                          test_cloud_workload)

        result = migrationTarget_get(targetVM)

        assert result['cloud_type'] == test_cloud_type
        assert result['username'] == test_username
        assert result['password'] == test_password
        assert result['domain'] == test_ipaddress.get_ipaddress()
        assert result['mountpoint'] == test_cloud_workload.storage

    def test_check_Mounts(self):
        """Function to test Service Layer to check mounts if 
           selected mount is present in provided mountpoints or no"""
        test_mountpoint1 = mountpoint_create('C:\\', 25)
        test_mountpoint2 = mountpoint_create('D:\\', 25)
        test_mountpoint3 = mountpoint_create('E:\\', 25)

        test_mountpoint_list = mountpoints_list(test_mountpoint1,
                                                test_mountpoint2,
                                                test_mountpoint3)

        test_selected_mountpoint = mountpoint_create('C:\\', 25)
        test_selected_mountpoint_list = [test_selected_mountpoint.get_mountPoint_instances()]

        result = check_Mounts(test_selected_mountpoint_list,
                              test_mountpoint_list)

        assert result['key'] == 'success'

    def test_check_Mounts_invalid(self):
        """Function to test Service Layer to check mounts if
           selected mount is present in provided mountpoints or no
           In this test case, it is not present"""
        test_mountpoint1 = mountpoint_create('C:\\', 25)
        test_mountpoint2 = mountpoint_create('D:\\', 25)
        test_mountpoint3 = mountpoint_create('E:\\', 25)

        test_mountpoint_list = mountpoints_list(test_mountpoint1,
                                                test_mountpoint2,
                                                test_mountpoint3)

        test_selected_mountpoint = mountpoint_create('F:\\', 25)
        test_selected_mountpoint_list = [test_selected_mountpoint.get_mountPoint_instances()]

        result = check_Mounts(test_selected_mountpoint_list,
                              test_mountpoint_list)

        assert result['key'] == 'error'

    def test_migration(self):
        """Function to test Service Layer to run migrations"""
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('1.1.1.1')
        sources = []
        creds1 = Credentials(test_username1,
                             test_password1,
                             test_ipaddress1.get_ipaddress())

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        test_MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, test_MountPoints_list1)
        sources.append(test_source1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)
        sources.append(test_source2)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        test_selected_mountpoint = MountPoint('C:\\', 25)
        test_selected_mountpoint_list = [test_selected_mountpoint.get_mountPoint_instances()]

        result = migration(test_selected_mountpoint_list,
                           test_source1, test_targetVM,
                           test_ipaddress1, sources, test_MountPoints_list1)

        print(result)

        assert result['key'] == 'success'
        assert result['migration_State'] == 'success'

    def test_migration_ip_address_Changed(self):
        """Function to test Service Layer to run migrations
           This case deals with IP address changed during workload """
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('1.1.1.1')
        sources = []
        creds1 = Credentials(test_username1,
                             test_password1,
                             '2.2.2.2')

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        test_MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, test_MountPoints_list1)
        sources.append(test_source1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)
        sources.append(test_source2)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        test_selected_mountpoint = MountPoint('C:\\', 25)
        test_selected_mountpoint_list = [test_selected_mountpoint.get_mountPoint_instances()]

        result = migration(test_selected_mountpoint_list,
                           test_source1, test_targetVM,
                           test_ipaddress1, sources, test_MountPoints_list1)

        print(result)

        assert result['key'] == 'error'
        assert result['migration_State'] == 'error'

    def test_migration_ip_address_Changed(self):
        """Function to test Service Layer to run migrations
           This case deals with sources with same address being not allowed"""
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('2.2.2.2')
        sources = []
        creds1 = Credentials(test_username1,
                             test_password1,
                             '2.2.2.2')

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        test_MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, test_MountPoints_list1)
        sources.append(test_source1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)
        sources.append(test_source2)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        test_selected_mountpoint = MountPoint('C:\\', 25)
        test_selected_mountpoint_list = [test_selected_mountpoint.get_mountPoint_instances()]

        result = migration(test_selected_mountpoint_list,
                           test_source1, test_targetVM,
                           test_ipaddress1, sources, test_MountPoints_list1)

        print(result)

        assert result['key'] == 'error'
        assert result['migration_State'] == 'error'

    def test_migration_ip_mount_not_present(self):
        """Function to test Service Layer to run migrations
           This case deals with if selected mount is NOT present in provided mountpoints"""
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('2.2.2.2')
        sources = []
        creds1 = Credentials(test_username1,
                             test_password1,
                             '2.2.2.2')

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        test_MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, test_MountPoints_list1)
        sources.append(test_source1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'D:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)
        sources.append(test_source2)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        test_selected_mountpoint = MountPoint('C:\\', 25)
        test_selected_mountpoint_list = [test_selected_mountpoint.get_mountPoint_instances()]

        result = migration(test_selected_mountpoint_list,
                           test_source1, test_targetVM,
                           test_ipaddress1, sources, test_MountPoints_list1)

        print(result)

        assert result['key'] == 'error'
        assert result['migration_State'] == 'error'
