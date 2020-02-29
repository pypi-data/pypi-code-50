from pvlv_interactions.configurations.configuration import *


class ActivatorBlockerElement(object):
    def __init__(self):
        self.triggers = []
        self.outputs = []
        self.author = None

    def extract_data(self, data):
        self.triggers = data.get('triggers', self.triggers)
        self.outputs = data.get('outputs', self.outputs)
        self.author = data.get('author')


class ReplyObjectData(object):
    def __init__(self, data):
        self.enabled = True
        self.mode = ReplyMode.NORMAL_MODE

        self.activators = []
        self.blockers = []

        self.__extract_data(data)

    @staticmethod
    def __build_list(item_list):
        out = []
        if item_list:
            for item in item_list:
                ab = ActivatorBlockerElement()
                ab.extract_data(item)
                out.append(ab)
        return out

    def __extract_data(self, data):
        if not data:
            return

        self.enabled = data.get('enabled', self.enabled)

        mode = data.get('mode')
        if ReplyMode.QUIET_MODE.value <= mode <= ReplyMode.SPAM_MODE.value:
            self.mode = ReplyMode(mode)

        activators = data.get('activators')
        self.activators = self.__build_list(activators)

        blockers = data.get('blockers')
        self.blockers = self.__build_list(blockers)


class Replies(object):
    def __init__(self, data):
        self.replies = []
        for key in data:
            self.replies.append(ReplyObjectData(data.get(key)))
