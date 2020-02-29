from pvlv_interactions.generators.bad_words_generator.bad_words_generator import BadWordsGenerator
from pvlv_interactions.generators.badass_sentences.badass_sentences import BadassSentences
from pvlv_interactions.static_reply.static_reply import StaticReply
from pvlv_interactions.configurations.configuration import ANALYZE_MAX_LENGTH


class Interactions(object):

    def __init__(self, text, language):
        self.__in_text = text
        self.__language = language

        self.__static_reply_data = {}

    def set_static_reply_data(self, data: dict):
        self.__static_reply_data = data

    def response(self):
        # don't analyze long messages
        if len(self.__in_text) > ANALYZE_MAX_LENGTH:
            return None

        output = ''

        if self.__static_reply_data:
            sr = StaticReply(self.__static_reply_data)
            output += sr.message_reply(self.__in_text)

        bwg = BadWordsGenerator()
        output += bwg.message_reply(self.__language, self.__in_text)

        bs = BadassSentences()
        output += bs.message_reply(self.__language, self.__in_text)

        return output
