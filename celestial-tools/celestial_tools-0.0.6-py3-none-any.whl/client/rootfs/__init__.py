import os
import subprocess

from celestial_tools.strings import Filesystems
from celestial_tools.client.system import cmdline


def get_fs_types(device_node: str):
    """
    Fetch a list of possible filesystem types

    :param device_node: The device node to query
    :return: a list of strings with the possible filesystem type, else None
    """
    if not os.path.exists(device_node):
        return None
    output = subprocess.check_output(
        ['''(eval $(blkid {} | awk ' {{ print $3 }} '); echo $TYPE)'''.format(device_node)],
        shell=True,
        executable='/bin/bash').decode().rstrip()
    if output == "":
        retval = []
    elif output == Filesystems.EXT2:
        # ext3 filesystems misidentify as ext2.  Consider both as possible outputs
        retval = [Filesystems.EXT2, Filesystems.EXT3]
    else:
        retval = [output]
    return retval


def install(rootfs_file: str, device_node: str, block_size_kb: int = 10, expected_fs: str = Filesystems.NONE):
    """
    Install rootfs_file into device_node

    :param rootfs_file: Location of the new rootfs to install
    :param device_node: Device node where the new rootfs_file will be installed
    :param block_size_kb: Block size passed to **dd** utility
    :param expected_fs: Expected filesystem format
    """
    if expected_fs is not None:
        fs_types = get_fs_types(rootfs_file)
        if expected_fs not in fs_types:
            raise ValueError("rootfs_file is type {}, expected {}".format(rootfs_file, expected_fs))
    result = subprocess.run([
        'dd',
        'if={}'.format(rootfs_file),
        'of={}'.format(device_node),
        'bs={}K'.format(block_size_kb)
    ])
    if result.returncode != 0:
        raise RuntimeError("Failed to update {} with {}".format(device_node, rootfs_file))


def get_boot_device(cmdline_file: str = "/proc/cmdline") -> str:
    """
    Retrieve the "root" parameter of "/proc/cmdline"

    :param cmdline_file: The location of the cmdline file (that we booted with)
    :return: the "root" parameter of "/proc/cmdline"
    """
    return cmdline.get_parameter("root", cmdline_file)


def set_boot_device(boot_device: str, cmdline_file: str = "/boot/cmdline"):
    """
    Update the "root" parameter of the "cmdline_file" to "boot_device"

    :param boot_device: The location of the new boot device node
    :param cmdline_file:  The location of the boot partition's commandline file
    """
    cmdline.set_parameter("root", boot_device, cmdline_file)


def dual_boot_update(rootfs_file: str,
                     dev_1: str,
                     dev_2: str,
                     cmdline_file: str = "/boot/cmdline",
                     expected_rootfs_format: str = None):
    """
    Update the dual-rootfs system with the provided parameters

    :param rootfs_file: The filesystem to be installed
    :param expected_rootfs_format: The expected rootfs format
    :param cmdline_file: The location of the boot partition's commandline file
    :param dev_1: the first rootfs device node in the dual-boot configuration
    :param dev_2: the second rootfs device node in the dual-boot configuration
    """
    if dev_1 == dev_2:
        raise ValueError("Boot devices cannot be identical")
    current_boot_dev = get_boot_device(cmdline_file=cmdline_file)
    if current_boot_dev == dev_1:
        target_boot_dev = dev_2
    elif current_boot_dev == dev_2:
        target_boot_dev = dev_1
    else:
        raise ValueError("current rootfs '{}' does not match dev_1 or dev_2".format(current_boot_dev))

    install(rootfs_file, target_boot_dev, expected_fs=expected_rootfs_format)

    set_boot_device(target_boot_dev, cmdline_file=cmdline_file)
