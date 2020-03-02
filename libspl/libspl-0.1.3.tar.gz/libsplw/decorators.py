import inspect
from .exceptions import BadParamType, BadReturnType
import typing
from itertools import zip_longest

TFunc = typing.TypeVar("TFunc")


def type_check(ignore_self=False) -> typing.Callable[[TFunc], TFunc]:
    def _type_check(func: TFunc) -> TFunc:
        annotations = func.__annotations__
        arg_names = inspect.getargs(func.__code__).args  # type: ignore

        def out_func(*args):
            for i, (arg_name, arg) in enumerate(zip_longest(arg_names, args)):
                if i == 0 and arg_name == "self" and ignore_self:
                    continue
                if arg_name is None:
                    raise TypeError(f"Too many arguments passed")
                if arg is None:
                    raise TypeError(f"Too few arguments passed")
                if arg_name not in annotations:
                    raise BadParamType(f"Parameter {arg_name} missing annotation")
                if not isinstance(arg, annotations[arg_name]):
                    raise BadParamType(
                        f"Parameter {arg_name} is of type "
                        f"'{type(arg)}', expected '{annotations[arg_name]}'"
                    )
            result = func(*args)
            if "return" not in annotations:
                if result is not None:
                    raise BadReturnType(f"Procedure returned value ({result!r})")
            elif not isinstance(result, annotations["return"]):
                raise BadReturnType(
                    f"Function returned value of type '{type(result).__name__}'"
                    f", expected type '{annotations['return'].__name__}'"
                )
            return result

        return typing.cast(TFunc, out_func)

    return _type_check
