#!/usr/bin/python

import re
from sys import argv

def get_declaration(variable_name, variable_value):
    if (isinstance(variable_value, str)):
        return variable_name + " = '" + variable_value + "'"
    elif(isinstance(variable_value, int) or isinstance(variable_value, float)):
        return variable_name + " = " + str(variable_value)

def find_class_instantiations(source_code, variable_name):
    regex = re.compile(variable_name + "\([^\)]*\)", re.MULTILINE)
    return re.finditer(regex, source_code)

def find_parameter(source_code, parameter_name):
    param_regex = re.compile("(, ?)?" + parameter_name + " ?= ?[^,)]*")
    return re.search(param_regex, source_code)

def declare_variable(source_code, variable_name, variable_value):
    lines = source_code.split("\n")
    lines.append(get_declaration(variable_name, variable_value))
    return "\n".join(lines)

def remove_class_instantiation_parameter(source_code, class_name, parameter_name, condition=None):
    offset = 0
    for class_instantiation in find_class_instantiations(source_code, class_name):
        old_instantiation = class_instantiation.group()
        match = find_parameter(old_instantiation, parameter_name)
        params_padded = class_name + "( " in old_instantiation

        if match:
            # get paramter value
            param_value = match.group().split("=")[1].strip()
            if param_value.isdigit(): param_value = int(param_value)
            elif param_value.isdecimal(): param_value = float(param_value)

            if condition is None or condition(param_value):
                match_start, match_end = match.span()
                new_instantiation = old_instantiation[:match_start] + old_instantiation[match_end:]
                # remove comma from second param if replaced first param
                if class_name + "(, " in new_instantiation:
                    if params_padded:
                        new_instantiation = new_instantiation.replace(class_name + "(,", class_name + "(")
                    else:
                        new_instantiation = new_instantiation.replace(class_name + "(, ", class_name + "(")
                elif class_name + "(," in new_instantiation:
                    new_instantiation = new_instantiation.replace(class_name + "(,", class_name + "(")
                start_removal = class_instantiation.span()[0] - offset
                end_removal = class_instantiation.span()[1] - offset
                source_code = source_code[:start_removal] + new_instantiation + source_code[end_removal:]
                offset += (len(old_instantiation) - len(new_instantiation))

    return source_code
        

def remove_comments(source_code):
    lines = source_code.split("\n")
    lines = [line for line in lines if not line.startswith("#")]
    return "\n".join(lines)

def remove_imports(source_code):
    lines = source_code.split("\n")
    lines = [line for line in lines if not line.startswith("from ")]
    return "\n".join(lines)

def replace_class(source_code, old_class_name, new_class_name, condition=None):
    if condition:
        original = source_code
        offset = 0
        for old_instantiation in find_class_instantiations(source_code, old_class_name):
            old_instantiation_text = old_instantiation.group()
            start = old_instantiation.span()[0] + offset
            end = old_instantiation.span()[1] + offset
            before = source_code[:start]
            after = source_code[end:]
            line = original[before.rindex("\n") if "\n" in before else 0: len(before) + len(old_instantiation_text) + (after.index("\n") if "\n" in after else len(after) - 1)]
            if condition({ "text": old_instantiation_text, "line": line }):
                new_instantiation = old_instantiation_text.replace(old_class_name, new_class_name)
                source_code = before + new_instantiation + after
                offset += len(new_instantiation) - len(old_instantiation_text)
        return source_code
    else:
        return source_code.replace(old_class_name + "(", new_class_name + "(")

def replace_variable_declaration(source_code, variable_name, new_variable_value):
    old_lines = source_code.split("\n")
    new_lines = []
    for line in old_lines:
        if (line.startswith(variable_name + ' =') or line.startswith(variable_name + '=')) :
            new_lines.append(get_declaration(variable_name, new_variable_value))
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

if __name__ == '__main__':
    cmd, fp, subcommand, param1, param2 = argv
    with open(fp) as f:
        source_code = f.read().decode()
    if (subcommand == "remove-comments"):
        source_code = remove_comments(source_code)
        with open(fp, "w") as f:
            f.write(source_code)
    elif (subcommand == "remove-imports"):
        source_code = remove_imports(source_code)
        with open(fp, "w") as f:
            f.write(source_code)
    elif (subcommand == "declare-variable"):
        source_code = declare_variable(source_code, param1, param2)
        with open(fp, "w") as f:
            f.write(source_code)