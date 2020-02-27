import typing
from .constants import INPUT_PROMPTS, TYPE_NAMES, COMPLEX_REGEX
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


def handle_input(type_name: str, var_name: str, env: dict) -> None:
    """Get input as specified and store the result in env"""
    input_type = system_identifier(type_name)
    if input_type in (str, int, float):
        rv = None
        while rv is None:
            try:
                rv = input_type(input(INPUT_PROMPTS[input_type]))
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv
    elif input_type == list:
        rv = None
        while rv is None:
            try:
                rv = input(INPUT_PROMPTS[input_type]).split(", ")
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv
    elif input_type == bool:
        rv = None
        while rv is None:
            try:
                rv = {"y": True, "yes": True, "n": False, "no": False}[
                    input(INPUT_PROMPTS[input_type]).lower()
                ]
            except Exception:
                print(f"That wasn't {TYPE_NAMES[input_type]}, try again")
        env[var_name] = rv
    elif input_type == complex:
        rv = None
        while rv is None:
            try:
                tmp = input(INPUT_PROMPTS[input_type]).replace(" ", "")
                match = re.fullmatch(
                    COMPLEX_REGEX, tmp
                )
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
        env[var_name] = rv
