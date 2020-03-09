import os
import logging
import platform
import warnings


from cvargparse import GPUParser, Arg, ArgFactory

from cvfinetune.parser.dataset_args import add_dataset_args
from cvfinetune.parser.model_args import add_model_args
from cvfinetune.parser.training_args import add_training_args


def default_factory(extra_list=[]):
	return ArgFactory(extra_list)


class FineTuneParser(GPUParser):
	def init_logger(self, simple=False, logfile=None):
		if not self.has_logging: return
		fmt = '{levelname:s} - [{asctime:s}] {filename:s}:{lineno:d} [{funcName:s}]: {message:s}'

		handler0 = logging.StreamHandler()
		handler0.addFilter(HostnameFilter())
		handler0.setFormatter(logging.Formatter("<{hostname:^10s}>: " + fmt, style="{"))

		filename = logfile if logfile is not None else f"{platform.node()}.log"
		self._file_handler = handler1 = logging.FileHandler(filename=filename, mode="w")
		handler1.setFormatter(logging.Formatter(fmt, style="{"))

		logger = logging.getLogger()
		logger.addHandler(handler0)
		logger.addHandler(handler1)
		logger.setLevel(getattr(logging, self.args.loglevel.upper(), logging.DEBUG))


	def __del__(self):
		try:
			self._file_handler.flush()
		except Exception as e:
			warnings.warn("Could not flush logs to file: {}".format(e))


	def __init__(self, *args, **kwargs):
		super(FineTuneParser, self).__init__(*args, **kwargs)

		add_dataset_args(self)
		add_model_args(self)
		add_training_args(self)


class HostnameFilter(logging.Filter):

	def filter(self, record):
		record.hostname = platform.node()
		return True
