import configparser as cfg
import logging


CONFIG_PATH = 'configs/pavlov.cfg'

parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

__beta = parser.getboolean('credentials', 'BETA', fallback=False)
__TOKEN = parser.get('credentials', 'TOKEN', fallback='')
__TOKEN_BETA = parser.get('credentials', 'TOKEN_BETA', fallback='')
TOKEN = __TOKEN_BETA if __beta else __TOKEN

OWNER_ID = parser.get('admin', 'OWNER_ID', fallback=111111111)
LOGGING_CHAT = parser.get('admin', 'LOGGING_CHAT', fallback=111111111)

DEBUG = parser.get('debug', 'DEBUG', fallback=False)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pavlov')

if DEBUG:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.ERROR)
