
def read_inputs(inputs_file):
    """ Load up an inputs file and parse it into a dictionary """

    params = {}

    # Read in the file
    with open(inputs_file, 'r') as f:
        file_data = f.readlines()

    for line in file_data:
        # print(line)
        # Ignore lines that are commented out
        if line.startswith('#'):
            continue

        # Remove anything after a #
        line = re.sub(r'#[^\n]*[\n]', '', line)

        parts = re.findall(r'^([^=]*)=(.*)$', line)

        # parts = line.split('=')
        # if len(parts) > 1:
        if parts:
            match = parts[0]
            key = match[0].strip()
            val = match[1].strip()

            # Convert to float/int as appropriate
            if isint(val):
                val = int(val)
            elif isfloat(val):
                val = float(val)

            params[key] = val

    # print(params)
    return params


def write_inputs(location, params, ignore_list=None, do_sort=True):
    """
     Write out a set of parameters to an inputs file
    """
    output_file = ''

    key_list = list(params.keys())
    if do_sort:
        key_list.sort()

    for key in key_list:
        if not ignore_list or key not in ignore_list:

            if isinstance(params[key], list):
                key_val = ' '.join([str(a) for a in params[key]])

            else:
                key_val = str(params[key])

            output_file += '\n' + key + '=' + key_val

    with open(location, 'w') as f:
        f.write(output_file)

