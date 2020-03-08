import sys

from celestial_tools.client import dual_rootfs_update


def dual_rootfs_update_cmdline():
    """
    Runs dual_rootfs_update from the cmdline, parsing the provided sys.argv.
    setup.py maps this function to `celestial_dual_rootfs_update`.

    One can also execute this file (dual_rootfs_update_cmdline.py) from the commandline to run the commandline script.
    """
    dual_rootfs_update(sys.argv[1:])


# Run the program when this file is executed
if __name__ == "__main__":
    dual_rootfs_update_cmdline()
