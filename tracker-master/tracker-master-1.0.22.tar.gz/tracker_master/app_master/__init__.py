import logging
import queue
import sys

import tracker_master.config as CFG
import tracker_master.util as util
from tracker_master.app_master.configure import MasterConfigure
from tracker_master.app_master.master import SlavesConfigurer
from tracker_master.app_master.master import TrackerMaster
from tracker_master.app_master.notifier import Notifier
from tracker_master.app_master.notifier import ZabbixNotifier
from tracker_master.app_master.slave_data_consumer import ConfigurerConsumer
from tracker_master.app_master.slave_data_consumer import MainConsumer
from tracker_master.app_master.slave_data_producer import SlaveReaderThread
from tracker_master.app_master.slave_data_producer import VirtualSlaveReaderThread
from tracker_master.model.Master import Master

DEFAULT_PROFILE_NAME = 'development'

SLAVE_QUEUE_BUFFER_MAX_SIZE = 0


def print_conf(_master):
    print_master_conf(_master)
    if _master:
        print_slave_conf(_master.get_slaves())


def print_help():
    print('init master - \tSet master group name and master name for current served object\n' \
          'init slaves - \tStart configuring slaves. When slave send signal it registered at the system\n' \
          '\t\t\t\tUse stop command to stop that process\n' \
          'init zabbix - \tCreate zabbix configuration for current master at the Zabbix server\n' \
          'show config - \tShow current master configuration\n' \
          'start \t\t- \tRun master\n' \
          'exit \t\t- \texit the program\n' \
          '? \t\t\t- \tshow help\n')


def print_master_conf(_master):
    if _master and isinstance(_master, Master) and _master.is_configured():
        print('## Master: \n# Group: %s\n# Name: %s\n' % (_master.uniq_group_name, _master.uniq_master_name))
    else:
        print('## Master: NOT INITIALIZED\n')


def print_slave_conf(_slaves):
    if _slaves and isinstance(_slaves, dict) and len(_slaves) > 0:
        print('## Slaves: %s slaves configured' % len(_slaves))
        for slave in _slaves.values():
            print('# %s %s' % (slave.zbx_slave_number, slave.hw_id))
        print()
    else:
        print('## Slaves: NOT INITIALIZED\n')


def get_slave_reader(msg_queue):
    if CFG.slave_type() == CFG.TYPE_VIRTUAL:
        return VirtualSlaveReaderThread(msg_queue)
    elif CFG.slave_type() == CFG.TYPE_REAL:
        return SlaveReaderThread(msg_queue)


if __name__ == "__main__":
    print_help()
    # Take profile name from args
    profile_name = None
    if len(sys.argv) == 1:
        profile_name = DEFAULT_PROFILE_NAME
    else:
        profile_name = sys.argv[1]
    print('### Profile: %s' % profile_name)

    # Read configure with profile
    CFG.read("../conf/app_master_config.yaml", profile_name)

    # Setup loggin
    util.setup_logging()
    logger = logging.getLogger(__name__)

    # Initializing main objects
    slave_message_queue = queue.Queue(SLAVE_QUEUE_BUFFER_MAX_SIZE)
    tracker_master = TrackerMaster()
    tracker_master.initialize()

    # Do work
    print_conf(tracker_master.get_master())
    while True:
        cmd = input()
        if cmd == 'init master':
            print_master_conf(tracker_master.get_master())
            master_group_name = input('Set master group name: ').strip()
            master_name = input('Set master name: ').strip()
            tracker_master.apply_configure(master_group_name, master_name)
            print_master_conf(tracker_master.get_master())
        elif cmd == 'init slaves':
            print_slave_conf(tracker_master.get_slaves())

            slave_configurer = SlavesConfigurer()
            p = get_slave_reader(slave_message_queue)
            c = ConfigurerConsumer(slave_message_queue, slave_configurer)
            p.start()
            c.start()

            while True:
                cmd = input()
                if cmd == 'stop':
                    c.stop_working()
                    p.stop_working()
                    tracker_master.apply_slave_configure(slave_configurer.slaves)
                    print_slave_conf(tracker_master.get_slaves())
                    break
        elif cmd == 'start':
            notifier = Notifier()
            p = get_slave_reader(slave_message_queue)
            c = MainConsumer(slave_message_queue, notifier)
            notifier.add_listener(ZabbixNotifier(tracker_master))  # todo make dict __name__: Notifier
            p.start()
            c.start()
        elif cmd == 'show config':
            print_conf(tracker_master.get_master())
        elif cmd == 'init zabbix':
            zabbix_configure = MasterConfigure(CFG.zbx_api_url(), CFG.zbx_user(), CFG.zbx_pwd())
            zabbix_configure.configure(tracker_master.get_master(), tracker_master.get_slaves(), force_create=True)
        elif cmd == 'exit':
            sys.exit()  # todo check resources
        elif cmd == '?':
            print_help()
