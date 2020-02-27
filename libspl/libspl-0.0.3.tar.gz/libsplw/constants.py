class TypeFlags:
    DEFAULT = 0b111
    ALLOW_POS = 0b001
    ALLOW_ZERO = 0b10
    ALLOW_NEG = 0b100


INPUT_PROMPTS = {
    str: "Please enter some text\n>>> ",
    int: "Please enter a whole number\n>>> ",
    float: "Please enter a number\n>>> ",
    list: "Please enter some values, separated by commas\n>>> ",
    bool: "[Y]es/[N]o\n>>> ",
    complex: "Please enter a complex number\n>>> ",
}
TYPE_NAMES = {
    str: "text",
    int: "a whole number",
    float: "a number",
    list: "a list of values",
    bool: "[Y]es or [N]o",
    complex: "a complex number",
}
TYPE_FLAG_NAMES = {
    TypeFlags.DEFAULT: "any {}",
    TypeFlags.ALLOW_POS: "a positive {}",
    TypeFlags.ALLOW_POS | TypeFlags.ALLOW_ZERO: "a positive {} or zero",
    TypeFlags.ALLOW_POS | TypeFlags.ALLOW_NEG: "a non-zero {}",
    TypeFlags.ALLOW_ZERO | TypeFlags.ALLOW_NEG: "a negative {} or zero",
    TypeFlags.ALLOW_NEG: "a negative {}",
}
COMPLEX_REGEX = r"((\+|\-?)\d+(\.\d+)?)??((\+|\-?)(\d+(\.\d+)?)?i)?"

