#coding=utf-8
import logging


class Logger:
    def __init__(self, className="UNKNOWN", logFileName=None):
        from cdnutil import config
        flevel = config.getPropertyValue("flog_level")
        clevel = config.getPropertyValue("slog_level")
        if logFileName is None:
            logFileName = config.getPropertyValue("log_file_name")

        if logFileName is None:
            logFileName = "log.log"

        logging.basicConfig()
        self.logger = logging.getLogger(className)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(process)d %(lineno)d %(message)s")
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(self.__getLogLevel(clevel))
        #设置文件日志
        fh = logging.FileHandler(logFileName)
        fh.setFormatter(fmt)
        fh.setLevel(self.__getLogLevel(flevel))
        # 这里必须要设置，否则fh不仅要输出log到文件，还要在控制台打印
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
        self.logger.propagate=False


    def getLogger(self):
        return self.logger

    def __getLogLevel(self, level):
        log_level = logging.WARNING
        if level == "INFO":
            log_level = logging.INFO
        elif level == "FATAL":
            log_level = logging.FATAL
        elif level == "DEBUG":
            log_level = logging.DEBUG
        elif level == "ERROR":
            log_level = logging.ERROR
        elif log_level == "WARNING":
            log_level = logging.CRITICAL

        return log_level
