from unittest import TestCase
from Python_Test_Migration.provider.python_test_migration \
    import Credentials, MountPoint, Workload, MigrationTarget, Migration
from Python_Test_Migration.provider.constant import IP_ADDRESS


class TestCredentials(TestCase):
    def test_create_get_credentials(self):
        """Function to unit test Class Credentials"""
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        creds1 = Credentials(test_username,
                             test_password,
                             test_ipaddress.get_ipaddress())

        assert creds1.get_Credentials()['username'] == test_username
        assert creds1.get_Credentials()['password'] == test_password
        assert creds1.get_Credentials()['domain'] == test_ipaddress.get_ipaddress()


class TestMountPoint(TestCase):
    def test_create_get_mountpoint(self):
        """Function to unit test class MountPPoint"""
        test_mountpoint_name = 'C:\\'
        test_mountpoint_size = 25
        mountpoint1 = MountPoint(test_mountpoint_name, test_mountpoint_size)

        assert mountpoint1.get_mountPoint_instances()['mount_name'] == test_mountpoint_name
        assert mountpoint1.get_mountPoint_instances()['size'] == test_mountpoint_size


class TestWorkload(TestCase):
    def test_create_get_Workload(self):
        """Function to unit test class Workload"""
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

        assert test_source.get_workload()['username'] == test_username
        assert test_source.get_workload()['password'] == test_password
        assert test_source.get_workload()['domain'] == test_ipaddress.get_ipaddress()
        assert test_source.get_workload()['mount_point'][0]['mount_name'] == test_mountpoint_name
        assert test_source.get_workload()['mount_point'][0]['size'] == test_mountpoint_size

    def test_check_constrains(self):
        """Function to unit test class Workload constrains method"""
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

        check_constrains = test_source.constrains(test_ipaddress.get_ipaddress())

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
        check_constrains = test_source.constrains(test_ipaddress.get_ipaddress())

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
        check_constrains = test_source.constrains(test_ipaddress.get_ipaddress())

        assert check_constrains['key'] == 'error'

    def test_check_checksourceip(self):
        """Function to unit test class Workload checksourceip method to detect sources with duplicate IP's"""
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('1.1.1.1')
        # changed_ip = '1.1.1.1'

        creds1 = Credentials(test_username1,
                             test_password1,
                             test_ipaddress1.get_ipaddress())

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, MountPoints_list1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')
        # changed_ip = '1.1.1.1'

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)

        source_ips = [test_source1.get_workload()['domain'], test_source2.get_workload()['domain']]

        result = test_source1.checksourceip(source_ips)

        assert result['key'] == 'success'

    def test_check_checksourceip_duplicate_ip_provided(self):
        """Function to unit test class Workload checksourceip method to detect sources with duplicate IP's
           Duplicate IP's provided in this case
        """
        test_username1 = "test_username"
        test_password1 = "test_passsword"
        test_ipaddress1 = IP_ADDRESS('2.2.2.2')
        # changed_ip = '1.1.1.1'

        creds1 = Credentials(test_username1,
                             test_password1,
                             test_ipaddress1.get_ipaddress())

        test_mountpoint_name1 = 'C:\\'
        test_mountpoint_size1 = 25
        mountpoint1 = MountPoint(test_mountpoint_name1, test_mountpoint_size1)
        MountPoints_list1 = [mountpoint1.get_mountPoint_instances()]

        test_source1 = Workload(creds1, MountPoints_list1)

        test_username2 = "test_username"
        test_password2 = "test_passsword"
        test_ipaddress2 = IP_ADDRESS('2.2.2.2')
        # changed_ip = '1.1.1.1'

        creds2 = Credentials(test_username2,
                             test_password2,
                             test_ipaddress2.get_ipaddress())

        test_mountpoint_name2 = 'C:\\'
        test_mountpoint_size2 = 25
        mountpoint2 = MountPoint(test_mountpoint_name2, test_mountpoint_size2)
        MountPoints_list2 = [mountpoint2.get_mountPoint_instances()]

        test_source2 = Workload(creds2, MountPoints_list2)

        source_ips = [test_source1.get_workload()['domain'], test_source2.get_workload()['domain']]

        result = test_source1.checksourceip(source_ips)

        assert result['key'] == 'error'


class TestMigrationTarget(TestCase):
    def test_create_get_migrationtarget(self):
        test_username = "test_username"
        test_password = "test_passsword"
        test_ipaddress = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username,
                                       test_password,
                                       test_ipaddress.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        targetVM = MigrationTarget(test_cloud_type,
                                   test_creds_cloud,
                                   test_cloud_workload)

        assert targetVM.get_Migration_Target()['cloud_type'] == test_cloud_type
        assert targetVM.get_Migration_Target()['username'] == test_username
        assert targetVM.get_Migration_Target()['password'] == test_password
        assert targetVM.get_Migration_Target()['domain'] == test_ipaddress.get_ipaddress()
        assert targetVM.get_Migration_Target()['mountpoint'] == test_cloud_workload.storage


class TestMigration(TestCase):
    def test_run_migration(self):
        """Method to test run migration"""
        test_username_src = "test_username"
        test_password_src = "test_passsword"
        test_ipaddress_src = IP_ADDRESS('2.2.2.2')

        creds1 = Credentials(test_username_src,
                             test_password_src,
                             test_ipaddress_src.get_ipaddress())

        test_mountpoint_name_src = 'C:\\'
        test_mountpoint_size_src = 25
        mountpoint1 = MountPoint(test_mountpoint_name_src, test_mountpoint_size_src)
        MountPoints_list = [mountpoint1.get_mountPoint_instances()]

        test_source = Workload(creds1, MountPoints_list)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        selected_mountpoint = MountPoint('C:\\', 25)
        selected_mountpoint_list = [selected_mountpoint.get_mountPoint_instances()]

        run_migration = Migration(selected_mountpoint_list, test_source, test_targetVM)
        status = run_migration.run(test_source, test_targetVM)

        # print(status)
        assert status['key'] == 'success'
        assert status['migration_State'] == 'success'

    def test_run_migration_with_C_not_allowed(self):
        """Method to test run migration with C not allowed"""
        test_username_src = "test_username"
        test_password_src = "test_passsword"
        test_ipaddress_src = IP_ADDRESS('2.2.2.2')

        creds1 = Credentials(test_username_src,
                             test_password_src,
                             test_ipaddress_src.get_ipaddress())

        test_mountpoint_name_src = 'D:\\'
        test_mountpoint_size_src = 25
        mountpoint1 = MountPoint(test_mountpoint_name_src, test_mountpoint_size_src)
        MountPoints_list = [mountpoint1.get_mountPoint_instances()]

        test_source = Workload(creds1, MountPoints_list)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target.get_ipaddress())

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        selected_mountpoint = MountPoint('D:\\', 25)
        selected_mountpoint_list = [selected_mountpoint.get_mountPoint_instances()]

        run_migration = Migration(selected_mountpoint_list, test_source, test_targetVM)
        status = run_migration.run(test_source, test_targetVM)

        # print(status)
        assert status['key'] == 'error'
        assert status['migration_State'] == 'error'

    def test_run_migration_error_during_migration(self):
        """Method to test run migration with some error happened during migration"""
        test_username_src = "test_username"
        test_password_src = "test_passsword"
        test_ipaddress_src = IP_ADDRESS('2.2.2.2')

        creds1 = Credentials(test_username_src,
                             test_password_src,
                             test_ipaddress_src)

        test_mountpoint_name_src = 'D:\\'
        test_mountpoint_size_src = 25
        mountpoint1 = MountPoint(test_mountpoint_name_src, test_mountpoint_size_src)
        MountPoints_list = [mountpoint1.get_mountPoint_instances()]

        test_source = Workload(creds1, MountPoints_list)

        test_username_target = "test_username"
        test_password_target = "test_passsword"
        test_ipaddress_target = IP_ADDRESS('2.2.2.2')

        test_creds_cloud = Credentials(test_username_target,
                                       test_password_target,
                                       test_ipaddress_target)

        test_cloud_type = 'azure'
        test_cloud_workload = Workload(test_creds_cloud)

        test_targetVM = MigrationTarget(test_cloud_type, test_creds_cloud, test_cloud_workload)

        selected_mountpoint = MountPoint('D:\\', 25)
        selected_mountpoint_list = [selected_mountpoint.get_mountPoint_instances()]

        run_migration = Migration(selected_mountpoint_list, test_source, test_targetVM)
        status = run_migration.run(test_source, test_targetVM)

        # print(status)
        assert status['key'] == 'error'
        assert status['migration_State'] == 'error'
