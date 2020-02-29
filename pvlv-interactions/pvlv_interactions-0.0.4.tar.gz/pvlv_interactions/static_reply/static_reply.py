from random import randrange
from pvlv_interactions.static_reply.modules.reply_object import (
    Replies,
    ReplyObjectData,
    ActivatorBlockerElement
)


class StaticReply(object):

    def __init__(self, data: dict):

        self.replies = Replies(data).replies

        self.text_array = []
        self.output = ''

    def __find_build_reply(self, abe: ActivatorBlockerElement):

        for trigger in abe.triggers:
            trig = trigger.lower().split(' ')
            if all(x in self.text_array for x in trig):
                i = randrange(len(abe.outputs))
                if abe.author:
                    return '{}\nCit: {}'.format(abe.outputs[i], abe.author)
                return abe.outputs[i]

    def __build_reply(self, reply: ReplyObjectData):

        out = ''
        for activator in reply.activators:
            res = self.__find_build_reply(activator)
            if res:
                out = res

        if not out:
            return ''

        for blocker in reply.blockers:
            res = self.__find_build_reply(blocker)
            if res:
                out = res

        self.output += out+'\n'

    def message_reply(self, text):

        self.text_array = text.split(' ')

        for reply in self.replies:
            self.__build_reply(reply)

        return self.output
