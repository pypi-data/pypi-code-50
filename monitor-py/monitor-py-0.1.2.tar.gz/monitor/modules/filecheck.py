import os, sys, pwd



######################
# need path for logs, config
#
#

#validate = validate(os.makedirs())

def validate(f):
    def _makedirs(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except FileExistsError:
            pass
    return _makedirs

@validate
def make_proj_dirpath(dir_path):
    os.makedirs(dir_path)

def root_warning():
    print('SCRIPT SHOULD NOT BE RUN AS ROOT!')
    sys.exit(1)

def check_files():
    """ If base directory isn't present it is created also checks individually for logs 
    and config dir and creates if needed
    """    
    # debug_logger = logger.get_logger()
    # debug_logger.debug('Checking for needed directories')
    # try block added to check if script is running as root
    # throws an error if it is unless running in a container (set by ENV variable in Dockerfile) which is build environment
    try:
        base_path = f'/home/{str(pwd.getpwuid(os.getuid())[0])}/monitor/'
    except OSError as e:
        if pwd.getpwuid(os.getuid())[0] == 0 and os.environ['CONTAINER'] == 'True':
            pass
        else:
            root_warning()
    else:
        make_proj_dirpath(os.path.join(base_path, 'logs'))
        make_proj_dirpath(os.path.join(base_path, 'config'))

check_files()
