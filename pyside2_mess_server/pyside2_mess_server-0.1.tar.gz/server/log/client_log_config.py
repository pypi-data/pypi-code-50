# Date: 22/09/2019 19:22
# Author: MaximRaduntsev

import sys
import logging.handlers
import os.path
from dynaconf import settings

# Подготовка имени файла для логирования
BASE_LOG_DIR_PATH = os.path.abspath(os.path.join(__file__, '../'))
LOG_PATH = os.path.join(BASE_LOG_DIR_PATH, 'log_storage/client.log')

# Создаем объект форматирования: <дата-время> <уровень важности> <имя
# модуля> <сообщение>
formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(module)s: %(message)s',
    '%Y-%m-%d %H:%M:%S')

# Создать обработчик, который выводит сообщения в поток stderr
stream = logging.StreamHandler(sys.stderr)
stream.setFormatter(formatter)
stream.setLevel(logging.ERROR)

# Создаем файловый обработчик логирования:
log_file = logging.FileHandler(LOG_PATH, encoding=settings.BASE_ENCODING)
log_file.setFormatter(formatter)

# Создать объект-логгер регистратор
logger = logging.getLogger('client')
# Добавляем в логгер новый обработчик событий и устанавливаем уровень
# логирования
logger.addHandler(log_file)
logger.addHandler(stream)
logger.setLevel(settings.LOGGING_LEVEL)

if __name__ == '__main__':
    logger.info('Тестовый запуск логирования')
    logger.critical('Тестовый запуск логирования')
    logger.error('Тестовый запуск логирования')
