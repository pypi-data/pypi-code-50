def read_command_structure(text):
    """
    :param text: must be a string
    :return: argument as string, parameters as tuple [parameter, data]

    example:
    mal the cat is on the table -f lol this is cute -d 12
    """
    text_list = text.split()

    trigger = text_list.pop(0)  # remove the command trigger
    arg = ''
    params = {}

    if len(text_list) is 1:
        arg = text_list[0]
        return trigger, arg, params

    read_params = False
    current_param = None
    while text_list:
        word = text_list.pop(0)

        if str.startswith(word, '-'):
            read_params = True
            current_param = word
            params[current_param] = ''

        elif read_params:
            params[current_param] += word + ' '

        else:
            arg += word + ' '

    return trigger, arg, params
