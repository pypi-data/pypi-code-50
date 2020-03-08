"""
Functions related to the cmdline file
"""


def load(cmdline_file) -> str:
    """
    Load the given cmdline file as a string

    :param cmdline_file: The cmdline file to load
    :return: A string containing the content of the cmdline file
    """
    contents = ""
    with open(cmdline_file, 'r') as fpt:
        for l in fpt.readlines():
            contents += l
    return contents


def write(parameters: dict, cmdline_file: str):
    """
    Create a cmdline file with the provided parameters
    Overwrite it if it exists

    :param parameters: A dictionary of key/value pairs
    :param cmdline_file: The **boot partition's** cmdline file
    """
    data = ""
    for key in parameters:
        if len(data) != 0:
            data += " "
        data += "{}={}".format(key, parameters[key])
    with open(cmdline_file, 'w') as fpt:
        fpt.write(data)


def get_parameters(cmdline_file: str) -> dict:
    """
    Retrieve all of the parameters of the cmdline file

    :param cmdline_file: The cmdline file to load
    :return: a list of {key: , value: }
    """
    contents = load(cmdline_file)
    entries = contents.split(" ")
    parameters = {}
    for e in entries:
        kvp = e.split("=")
        if len(kvp) == 2:
            parameters[kvp[0]] = kvp[1]
    return parameters


def get_parameter(parameter_name: str, cmdline_file: str) -> str:
    """
    Retrieve a parameter from the provided cmdline file

    :param parameter_name: The "key" to get from the cmdline file
    :param cmdline_file: The **kernel's** cmdline file
    :return: {key: value}
    """
    parameters = get_parameters(cmdline_file)
    if parameter_name in parameters:
        return parameters[parameter_name]
    return None


def set_parameter(parameter_name, parameter_value, cmdline_file):
    """
    Set a parameter in the provided cmdline file.  Create it if it doesn't exist,
    overwrite it if it does exist

    :param parameter_name: The "key" in the key value pair
    :param parameter_value: The value to set the key  to
    :param cmdline_file: location of the **boot partition's** cmdline file
    """
    parameters = get_parameters(cmdline_file)
    parameters[parameter_name] = parameter_value
    write(parameters, cmdline_file)
