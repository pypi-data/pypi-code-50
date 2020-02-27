import typing
from .constants import (
    INPUT_PROMPTS,
    TYPE_NAMES,
    TYPE_FLAG_NAMES,
    COMPLEX_REGEX,
    TypeFlags,
)
from .exceptions import InvalidTypeError
import re


def system_identifier(name: str) -> typing.Optional[type]:
    """Get a Python type from its SPLW name"""
    rv: typing.Optional[type] = None
    if name in ["str", "STR", "Str", "string", "STRING", "String"]:
        rv = str
    if name in ["int", "INT", "Int", "integer", "INTEGER", "Integer"]:
        rv = int
    if name in [
        "float",
        "FLOAT",
        "Float",
        "real",
        "REAL",
        "Real",
        "number",
        "NUMBER",
        "Number",
    ]:
        rv = float
    if name in [
        method(i)
        for method in (str.upper, str.lower, str.title)
        for i in ("list", "array", "tuple")
    ]:
        rv = list
    if name in ["bool", "BOOL", "Bool", "boolean", "BOOLEAN", "Boolean"]:
        rv = bool
    if name in ["complex", "Complex", "COMPLEX"]:
        rv = complex
    return rv


def get_flags(type_flags: str) -> int:
    """Get the type flags from a type flag string"""
    if type_flags in ["POS", "POSITIVE"]:
        return TypeFlags.ALLOW_POS
    if type_flags in ["NONNEG", "NONNEGATIVE"]:
        return TypeFlags.ALLOW_POS | TypeFlags.ALLOW_ZERO
    if type_flags == "NONZERO":
        return TypeFlags.ALLOW_POS | TypeFlags.ALLOW_NEG
    if type_flags in ["NONPOS", "NONPOSITIVE"]:
        return TypeFlags.ALLOW_NEG | TypeFlags.ALLOW_ZERO
    if type_flags in ["NEG", "NEGATIVE"]:
        return TypeFlags.ALLOW_NEG
    raise InvalidTypeError("Invalid type flag: " + repr(type_flags))


def obeys_flags(number: typing.Union[int, float], flags: int) -> bool:
    if flags & TypeFlags.ALLOW_ZERO and number == 0:
        return True
    if flags & TypeFlags.ALLOW_POS and number > 0:
        return True
    if flags & TypeFlags.ALLOW_NEG and number < 0:
        return True
    return False


def handle_input(type_name: str) -> typing.Any:
    """Get input as specified"""
    split_type = type_name.split(" ")
    if len(split_type) > 1:
        if len(split_type) > 2:
            raise InvalidTypeError(
                repr(type_name)
                + " has too many words: "
                + str(len(split_type))
                + " (max 2)"
            )
        input_type = system_identifier(split_type[1])
        if input_type not in (int, float):
            raise InvalidTypeError(
                repr(split_type[1].upper()) + " cannot receive type flags"
            )
        flags = get_flags(split_type[0])
    else:
        input_type = system_identifier(type_name)
        flags = TypeFlags.DEFAULT
    if input_type in (str, int, float):
        rv = None
        while rv is None:
            try:
                rv = input_type(input(INPUT_PROMPTS[input_type]))
                if input_type in (int, float):
                    if not obeys_flags(rv, flags):
                        print(
                            f"That wasn't {TYPE_FLAG_NAMES[flags].format(TYPE_NAMES[input_type][2:])}, try again"
                        )
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        return rv
    elif input_type == list:
        rv = None
        while rv is None:
            try:
                rv = input(INPUT_PROMPTS[input_type]).split(", ")
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        return rv
    elif input_type == bool:
        rv = None
        while rv is None:
            try:
                rv = {"y": True, "yes": True, "n": False, "no": False}[
                    input(INPUT_PROMPTS[input_type]).lower()
                ]
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        return rv
    elif input_type == complex:
        rv = None
        while rv is None:
            try:
                tmp = input(INPUT_PROMPTS[input_type]).replace(" ", "")
                match = re.fullmatch(COMPLEX_REGEX, tmp)
                if not match:
                    print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
                    continue
                # [print(match.group(i)) for i in range(7)]
                real = int(match.group(1) or 0)
                imag = int(
                    (match.group(5) + (match.group(6) or "1"))
                    if match.group(5)
                    else "0"
                )
                rv = complex(real, imag)
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        return rv
