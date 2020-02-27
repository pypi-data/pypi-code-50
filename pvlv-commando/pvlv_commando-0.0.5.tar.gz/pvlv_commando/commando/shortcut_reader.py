from pvlv_commando.commando.modules.base_command_reader import BaseCommandReader


class ShortcutCommandReader(BaseCommandReader):
    def __init__(self):
        super(ShortcutCommandReader, self).__init__()
        self._dependency = None
        self._sub_call = None

    def read_command(self, language, module):

        if module is None:
            raise Exception('Command: {} do not exist'.format(module))
        else:
            self._dependency = module.get('dependency')
            self._sub_call = module.get('sub_call')

            self._invocation_words = self._read_language(language, module.get('invocation_words'))
            self._description = self._read_language(language, module.get('description'))