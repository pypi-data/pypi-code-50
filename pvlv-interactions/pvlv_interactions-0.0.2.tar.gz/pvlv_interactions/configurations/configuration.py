import configparser as cfg
import logging


CONFIG_PATH = 'configs/interactions.cfg'

parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

ANALYZE_MAX_LENGTH = parser.get('text', 'ANALYZE_MAX_LENGTH', fallback=30)

DEBUG = parser.get('debug', 'DEBUG', fallback=False)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pvlv_commando')

if DEBUG:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.ERROR)
