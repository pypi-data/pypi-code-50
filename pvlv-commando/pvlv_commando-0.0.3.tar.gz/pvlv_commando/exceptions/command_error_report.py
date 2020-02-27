from pvlv_commando.commando.command_descriptor import CommandDescriptor


def command_error_report(
        public_exc: str,
        full_exc: str,
        command_descriptor: CommandDescriptor,
        arg,
        params,
    ):

    out = 'Error during Command execution:\n'
    out += 'MODULE: {}\n'.format(command_descriptor.module)
    out += 'NAME: {}\n'.format(command_descriptor.name)
    if arg:
        out += 'ARG: {}\n\n'.format(arg)
    if params:
        out += 'PARAMS LIST:\n'
        for key in params.keys():
            out += '-{}: {}\n'.format(key, params.get(key))
        out += '\n'
    out += 'PUBBLIC ERROR: {}\n'.format(public_exc)
    out += 'FULL ERROR:\n{}\n'.format(full_exc)

    return out
