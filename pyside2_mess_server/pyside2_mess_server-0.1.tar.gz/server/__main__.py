# -*- coding: utf-8 -*-
# Date: 06.02.2020
# Author: MaximRaduntsev
import os
from dynaconf import settings
from config.settings import __file__ as config1_file

f1 = os.path.join(os.path.dirname(config1_file), 'settings.py')
os.environ['SETTINGS_MODULE_FOR_DYNACONF'] = f1

if __name__ == "__main__":
    print(settings.RESPONSE_OK)
