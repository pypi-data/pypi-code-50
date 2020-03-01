import os, sys



######################
# need path for logs, config
#
#
def check_files():
    """ If base directory isn't present it is created also checks individually for logs 
    and config dir and creates if needed
    """    
    # debug_logger = logger.get_logger()
    # debug_logger.debug('Checking for needed directories')
    # try block added to check if script is running as root
    # throws an error if it is unless running in a container (set by ENV variable in Dockerfile) which is build environment
    try:
        base_path = f'/home/{os.getlogin()}/monitor/'
    except OSError as e:
        if os.getuid() == 0 and os.environ['CONTAINER']:
            pass
        else:
            print('SCRIPT SHOULD NOT BE RUN AS ROOT!')
            sys.exit(1)
    if not os.path.exists(base_path):
        # debug_logger.debug('Base Path not found, creating logs and config directories')
        # create log directory
        os.makedirs(os.path.join(base_path, 'logs'))
        # create settings directory
        os.makedirs(os.path.join(base_path, 'config'))
    elif not os.path.exists(os.path.join(base_path, 'logs')):
        os.makedirs(os.path.join(base_path, 'logs'))
    elif not os.path.exists(os.path.join(base_path, 'config')):
        os.makedirs(os.path.join(base_path, 'config'))


check_files()
