__version__ = "0.2.0"

from cvargparse.argument import Argument
from cvargparse.argument import FileArgument
Arg = Argument

from cvargparse.factory import ArgFactory
from cvargparse.factory import BaseFactory
from cvargparse.parser import BaseParser
from cvargparse.parser import GPUParser

__all__ = [
	"Arg",
	"Argument",
	"FileArgument",
	"ArgFactory",
	"BaseFactory",
	"BaseParser",
	"GPUParser",
]
