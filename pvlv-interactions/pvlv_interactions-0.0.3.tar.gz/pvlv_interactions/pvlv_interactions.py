from pvlv_interactions.generators.bad_words_generator.bad_words_generator import BadWordsGenerator
from pvlv_interactions.generators.badass_sentences.badass_sentences import BadassSentences
from pvlv_interactions.configurations.configuration import ANALYZE_MAX_LENGTH


class Interactions(object):

    def __init__(self, text, language):
        self.in_text = text
        self.language = language

    def response(self):
        # don't analyze long messages
        if len(self.in_text) > ANALYZE_MAX_LENGTH:
            return None

        output = ''

        bwg = BadWordsGenerator()
        output += bwg.message_reply(self.language, self.in_text)

        bs = BadassSentences()
        output += bs.message_reply(self.language, self.in_text)

        return output
