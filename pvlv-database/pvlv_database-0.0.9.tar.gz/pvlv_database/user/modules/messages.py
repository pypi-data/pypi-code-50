from pvlv_database.common.action_counter_log import ActionCounterLog
from pvlv_database.configurations.configuration import MAX_RETENTION_TEXT


class MessagesData(object):

    def __init__(self):

        self.msg_log = ActionCounterLog()
        self.img_log = ActionCounterLog()
        self.links_log = ActionCounterLog()
        self.vocals_log = ActionCounterLog()

        self.swear_words_log = ActionCounterLog()
        self.swear_words = {}

        self.most_used_words = {}

        self.text_log = []

    def extract_data(self, raw_data):

        msg_log = raw_data.get('msg_log')
        self.msg_log = ActionCounterLog() if not msg_log else ActionCounterLog().extract_data(msg_log)

        img_log = raw_data.get('img_log')
        self.img_log = ActionCounterLog() if not img_log else ActionCounterLog().extract_data(img_log)

        links_log = raw_data.get('links_log')
        self.links_log = ActionCounterLog() if not links_log else ActionCounterLog().extract_data(links_log)

        vocals_log = raw_data.get('vocals_log')
        self.vocals_log = ActionCounterLog() if not vocals_log else ActionCounterLog().extract_data(vocals_log)

        swear_words_log = raw_data.get('swear_words_log')
        self.swear_words_log = ActionCounterLog() if not swear_words_log else ActionCounterLog().extract_data(swear_words_log)

        self.swear_words = raw_data.get('swear_words', self.swear_words)

        self.most_used_words = raw_data.get('most_used_words', self.most_used_words)

        self.text_log = raw_data.get('text_log', self.text_log)

        return self

    def build_data(self):

        data_out = {

            'msg_log': self.msg_log.build_data(),
            'img_log': self.img_log.build_data(),
            'links_log': self.links_log.build_data(),
            'vocals_log': self.vocals_log.build_data(),

            'swear_words_log': self.swear_words_log.build_data(),
            'swear_words': self.swear_words,

            'most_used_words': self.most_used_words,

            'text_log': self.text_log,
        }

        return data_out

    def update_msg_log(self, value: tuple):
        self.msg_log.update_log_by_hour(value)
        self.msg_log.update_log_by_day(value)
        self.msg_log.update_log_by_month(value)

    def update_img_log(self, value: tuple):
        self.img_log.update_log_by_hour(value)
        self.img_log.update_log_by_day(value)
        self.img_log.update_log_by_month(value)

    def update_links_log(self, value: tuple):
        self.links_log.update_log_by_hour(value)
        self.links_log.update_log_by_day(value)
        self.links_log.update_log_by_month(value)

    def update_vocals_log(self, value: tuple):
        self.vocals_log.update_log_by_hour(value)
        self.vocals_log.update_log_by_day(value)
        self.vocals_log.update_log_by_month(value)

    def update_swear_words_log(self, value: tuple):
        self.swear_words_log.update_log_by_hour(value)
        self.swear_words_log.update_log_by_day(value)
        self.swear_words_log.update_log_by_month(value)

    def update_text_log(self, text: str):
        """
        :param text: the test message

        Calculate the hash of the text
        append to the text_log:
        - text
        - len
        - simple_hash_code
        """
        simple_hash_code = 0
        for char in text.lower():
            simple_hash_code += ord(char)

        self.text_log.insert(0, [text, len(text), simple_hash_code])

        if len(self.text_log) > MAX_RETENTION_TEXT:
            self.text_log.pop()

    def is_message_spamming(self):
        """
        Check if the last item added is equal to the last 5 items in the messages
        :return:
        """
        equal_counter = 1
        last_el = self.text_log[0]

        if last_el[1] <= 3:
            equal_trigger = 5
        elif last_el[1] <= 8:
            equal_trigger = 4
        elif last_el[1] <= 12:
            equal_trigger = 3
        else:
            equal_trigger = 2

        for el in self.text_log[1:5]:
            if last_el[2] == el[2] and last_el[1] == el[1]:
                equal_counter += 1

        if equal_counter >= equal_trigger:
            return True
        else:
            return False
