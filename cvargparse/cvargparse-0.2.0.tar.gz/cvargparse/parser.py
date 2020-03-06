import argparse
import logging

from cvargparse.argument import Argument as Arg
from cvargparse.factory import BaseFactory

class BaseParser(argparse.ArgumentParser):

	def __init__(self, arglist=[], nologging=False, sysargs=None, *args, **kw):
		self.__nologging = nologging
		self.__sysargs = sysargs
		self._groups = {}

		super(BaseParser, self).__init__(*args, **kw)

		self.add_args(arglist)

		if not self.has_logging: return

		group = self.add_argument_group("Logger arguments")
		group.add_argument(
			'--logfile', type=str, default='',
			help='file for logging output')

		group.add_argument(
			'--loglevel', type=str, default='INFO',
			help='logging level. see logging module for more information')

		self.__args = None


	def get_group(self, name):
		return self._groups.get(name)

	def has_group(self, name):
		return name in self._groups


	def add_argument_group(self, title, *args, **kwargs):
		group = super(BaseParser, self).add_argument_group(title=title, *args, **kwargs)
		self._groups[title] = group
		return group


	def add_args(self, arglist, group_name=None, group_kwargs={}):

		if isinstance(arglist, BaseFactory):
			arglist = arglist.get()

		if group_name is None:
			group = self
		elif self.has_group(group_name):
			group = self.get_group(group_name)
		else:
			group = self.add_argument_group(group_name, **group_kwargs)

		for arg in arglist:
			if isinstance(arg, Arg):
				group.add_argument(*arg.args, **arg.kw)
			else:
				group.add_argument(*arg[0], **arg[1])

	@property
	def args(self):
		if self.__args is None:
			self.__args = self.parse_args(self.__sysargs)

		return self.__args


	@property
	def has_logging(self):
		return not self.__nologging

	def init_logger(self, simple=False):
		if not self.has_logging: return
		fmt = '%(message)s' if simple else '%(levelname)s - [%(asctime)s] %(filename)s:%(lineno)d [%(funcName)s]: %(message)s'
		logging.basicConfig(
			format=fmt,
			level=getattr(logging, self.args.loglevel.upper(), logging.DEBUG),
			filename=self.args.logfile or None,
			filemode="w")


class GPUParser(BaseParser):
	def __init__(self, *args, **kw):
		super(GPUParser, self).__init__(*args, **kw)
		self.add_argument(
			"--gpu", "-g", type=int, nargs="+", default=[-1],
			help="which GPU to use. select -1 for CPU only")
