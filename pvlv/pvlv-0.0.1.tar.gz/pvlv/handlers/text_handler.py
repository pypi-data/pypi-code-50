from pvlv.handlers.base_handler import BaseHandler


class TextHandler(BaseHandler):
    """
    It will handle the operations on the text.
    """
    def __init__(self, bot_interface):
        super().__init__(bot_interface)

    def handle(self, text):

        self.stats_updater.update_text(text)  # update stats

        if not self.check_commands(text):
            self.check_spam()

        self.check_level_up()
