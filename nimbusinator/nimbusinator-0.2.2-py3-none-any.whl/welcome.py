import platform
from psutil import virtual_memory

def welcome(cmd, nim):
    """RM Nimbus Welcome Screen

    This simulates the original Welcome Screen shown when the
    Nimbus is switched on and is waiting to boot from a disk.

    Your computer's memory size will be reported to keep things
    authentic.  Your Python version will substitute for
    Nimbus firmware version and the version number of your OS
    will be used as the machine serial number.

    After the Welcome Screen we imitate the old MS-DOS loading
    covfefe by printing the name of your OS and then the full
    version string of your Python distro.

    Oh, and turn up your speakers to hear the floppy drive :D

    """

    # Get Python version
    py_version = '{}.{}.{}'.format(
        platform.sys.version_info.major,
        platform.sys.version_info.minor, 
        platform.sys.version_info.micro
    )
    # Get memory stats
    mem = virtual_memory()
    total_mem = int(mem.total / 1024 / 1024)
    used_mem = int(mem.used / 1024 / 1024)
    free_mem = int(mem.free / 1024 / 1024)
    # Set up screen
    cmd.set_mode(80)
    cmd.set_colour(0, 0)
    cmd.set_colour(1, 9)
    cmd.set_border(1)
    # Frame
    cmd.area([(0, 0), (639, 0), (639, 249), (0, 249), (0, 0)], brush=2)
    cmd.area([(3, 2), (636, 2), (636, 247), (3, 247), (3, 2)], brush=1)
    # Nimbus logo with frame
    xl = 10
    yl = 212
    frame = [
        (xl, yl),
        (xl+304, yl),
        (xl+304, yl+32),
        (xl, yl+32),
        (xl, yl)
    ]
    cmd.plonk_logo((xl, yl))
    cmd.line(frame, brush=2)
    # Welcome
    cmd.plot('Welcome', (238, 145), size=3, brush=0, font=1)
    cmd.plot('Welcome', (236, 147), size=3, brush=2, font=1)
    # Memory
    cmd.plot('total memory size {m: >5} Mbytes'.format(m=total_mem), (15, 5), brush=0, font=1)
    cmd.plot('used  memory size {m: >5} Mbytes'.format(m=used_mem), (15, 15), brush=0, font=1)
    cmd.plot('main  memory size {m: >5} Mbytes'.format(m=free_mem), (15, 25), brush=0, font=1)
    # Version info
    cmd.area([(393, 4), (632, 4), (632, 30), (393, 30), (393, 4)], brush=2)
    cmd.area([(395, 5), (629, 5), (629, 29), (395, 29), (395, 5)], brush=3)
    cmd.plot('Firmware version: {}'.format(py_version), (400, 16), brush=0, font=1)
    cmd.plot('Serial number: {}'.format(platform.release()[:8]), (400, 6), brush=0, font=1)
    # Please supply an operating system
    cmd.plot('Please supply an operating system', (188, 100), brush=3, font=1)
    nim.sleep(1.3)
    cmd.plot('Please supply an operating system', (188, 100), brush=1, font=1)
    # Looking for an operating system
    cmd.plot('Looking for an operating system - please wait', (140, 100), brush=3, font=1)
    nim.run_floppy(True)
    nim.sleep(2)
    # Loading operating system
    cmd.plot('Looking for an operating system - please wait', (140, 100), brush=1, font=1)
    cmd.plot('Loading operating system', (224, 100), brush=3, font=1)
    nim.sleep(4)
    # Pretend DOS boot sequence
    cmd.set_mode(80)
    cmd.set_colour(0, 0)
    cmd.cls()
    cmd.set_cursor(True)
    nim.sleep(1.3)
    os_string = '{} - Version {}'.format(platform.system(), platform.release())
    os_string = os_string[:70]
    os_string = '   {}   '.format(os_string)
    # print os string in a groovy box thing
    bar = ''
    for i in range(0, len(os_string)):
        bar += ' '
    cmd.set_paper(3)
    cmd.set_pen(0)
    cmd.print(bar)
    cmd.print(os_string)
    cmd.print(bar)
    cmd.set_paper(0)
    cmd.set_pen(3)
    cmd.print(' ')
    nim.sleep(1.7)
    python_version = 'Python {}'.format(platform.sys.version)
    for text in python_version.split('\n'):
        cmd.print(text)
    nim.sleep(3.2)
    nim.run_floppy(False)
    nim.sleep(1.2)
    cmd.set_cursor(False)
    # Done
