import abc

from cvargparse import Arg
from cvfinetune.parser.utils import DEFAULT_INFO_FILE
from cvfinetune.parser.utils import get_info_file
from cvfinetune.parser.utils import parser_extender

@parser_extender
def add_dataset_args(parser):

	info_file = get_info_file()

	if info_file is None:
		_args = [
			Arg("data"),
			Arg("dataset"),
			Arg("parts")]
	else:
		_args = [
			Arg("data", default=DEFAULT_INFO_FILE),
			Arg("dataset", choices=info_file.DATASETS.keys()),
			Arg("parts", choices=info_file.PARTS.keys()),
		]

	_args.extend([

		Arg("--label_shift", type=int, default=1,
			help="label shift"),

		Arg("--swap_channels", action="store_true",
			help="preprocessing option: swap channels from RGB to BGR"),

	])

	parser.add_args(_args, group_name="Dataset arguments")

class DatasetParserMixin(abc.ABC):
	def __init__(self, *args, **kwargs):
		super(DatasetParserMixin, self).__init__(*args, **kwargs)
		add_dataset_args(self)


__all__ = [
	"DatasetParserMixin",
	"add_dataset_args"
]
