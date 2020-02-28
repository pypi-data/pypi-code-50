from pvlv.handlers.base_handler import BaseHandler


class ImgHandler(BaseHandler):
    """
    It will handle the operations on images.
    """
    def __init__(self, bot_interface):
        super().__init__(bot_interface)

    def handle(self, img=None, text=''):

        self.stats_updater.update_image()  # update stats

        if text:
            self.stats_updater.update_text(text)
            self.check_commands(text)
        self.check_level_up()
