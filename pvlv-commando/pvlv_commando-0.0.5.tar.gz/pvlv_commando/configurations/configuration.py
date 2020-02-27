import configparser as cfg
import logging


CONFIG_PATH = 'configs/commando.cfg'


parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

COMMANDS_DIR = parser.get('commands', 'COMMANDS_DIR', fallback='commands/')
WITH_MODULES = parser.get('commands', 'COMMANDS_DIR', fallback=True)
DEBUG = parser.get('debug', 'DEBUG', fallback=False)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pvlv_commando')

if DEBUG:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.ERROR)


# Languages Handled for messages
ENG = 'eng'
ITA = 'ita'
