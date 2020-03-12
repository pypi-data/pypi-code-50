import inspect
import logging


class StructuredMessage(object):
    """docstring for StructuredMessage"""

    def __init__(self, subject, detail):
        super(StructuredMessage, self).__init__()
        self.subject = subject
        self.detail = detail

    def __str__(self):
        return '{}  {}'.format(self.subject, self.detail)


class Log(object):
    def __init__(self, log_name):
        self.log_name = log_name
        self.logger = self.init_log()
        self._ = StructuredMessage

    def init_log(self):
        logger = logging.Logger(self.log_name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh = logging.FileHandler('Log/' + self.log_name + '.log')
        fh.setFormatter(formatter)
        # todo add json part of log later, for elk search
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    def info(self, subject, detail=''):
        self.log_dynamic_information()
        self.logger.info(self._(subject, detail))

    def error(self, subject, detail=''):
        self.log_dynamic_information()
        self.logger.error(self._(subject, detail))

    def warn(self, subject, detail=''):
        self.log_dynamic_information()
        self.logger.warn(self._(subject, detail))

    def log_dynamic_information(self):
        parent = inspect.stack()
        frame, file_path, line, method, _, _ = parent[3]
        source_file = file_path.split("\\")[-1]
        cls_name = frame.f_locals.get("self").__class__.__name__
        print('{} - {} - {} -{}'.format(source_file, line, cls_name, method))
