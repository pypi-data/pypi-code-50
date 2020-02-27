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
COMPLEX_REGEX = r"((\+|\-?)\d+(\.\d+)?)??((\+|\-?)(\d+(\.\d+)?)?i)?"
