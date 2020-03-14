# -*- coding: utf-8 -*-
"""
Created on 2017-5-7

@author: cheng.li
"""

import logging


class CustomLogger:
    def __init__(self,
                 logger_name: str,
                 log_level: str,
                 log_file: str = None):
        """
        Initialize the logger

        :param logger_name: str
        :param log_level: srt
        :param log_file: str
        """
        self.logger = logging.getLogger(logger_name)
        ch = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        if log_file:
            fh = logging.FileHandler(log_file)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        self.set_level(log_level)

    def set_level(self, log_level: str):
        if log_level.lower() == "info":
            self.logger.setLevel(logging.INFO)
        elif log_level.lower() == "warning":
            self.logger.setLevel(logging.WARNING)
        elif log_level.lower() == 'critical':
            self.logger.setLevel(logging.CRITICAL)
        elif log_level.lower() == 'debug':
            self.logger.setLevel(logging.DEBUG)

    def info(self, msg: str):
        self.logger.info(msg)

    def warning(self, msg: str):
        self.logger.warning(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def critical(self, msg: str):
        self.logger.critical(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)
