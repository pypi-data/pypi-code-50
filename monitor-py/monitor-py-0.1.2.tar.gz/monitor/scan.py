import os, sys
import subprocess
import json
import monitor.modules.logs as logger
# import modules.suppress as sp
import time as t
import monitor.modules.filecheck

_logger = logger.get_logger(__name__)


def load_config():
    """ Loads json config file and returns
    """
    config_file = f'/home/{os.getlogin()}/monitor/config/monitor.json' 
    try:
        with open(f'{config_file}', 'r') as f:
            config = json.load(f)
    except (IOError, json.decoder.JSONDecodeError) :
        _logger.debug('Config file missing, creating default')
        config = {'settings' : {'interval' : '60', 'servers' : ['localhost',]}}
        
        subprocess.call(['touch', f'{config_file}'], False)
        f = open(config_file, 'w')
        json.dump(config,f)
        f.close()
        _logger.info('Config File Saved')
    else:
        _logger.debug('Config File Loaded')
        config = json.dumps(config)
        config = json.loads(config)
    return config


def ping_server(host):
    """ Pings all servers in the passed list and logs if they are up or down
    
    Arguments:
        host {list} -- [list of hosts to ping]
    """    
        # with s.suppress_stdout():
    response = subprocess.call(['ping',f'{host}','-c','1',"-W","3"], False)
    return response

def main():
    config = load_config()
    # config = {
        # 'settngs' : [{'interval' : '60', 'servers' : ['localhost',]}]
        # }
    # config = json.dumps(config)

    while True:
        for s in config['settings']['servers']:
            response = ping_server(s)
            if response == 0:
                _logger.info(f'{s} is up...')
            elif response == 1:
                _logger.info(f'{s} is down...')
        interval = int(config['settings']['interval'])
        t.sleep(interval)



if __name__ == "__main__":
    main()