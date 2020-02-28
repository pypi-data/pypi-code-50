
class BotInterface:
    def __init__(self):

        self.user_id = None
        self.username = None

        self.guild_id = None
        self.guild_name = None

        self.timestamp = None

    def send_text(self, location, text, parse_mode=False):
        pass

    def reply_text(self, text, parse_mode=False):
        pass

    def send_photo(self, location, picture):
        pass

    def reply_photo(self, picture):
        pass

    def send_file(self, file):
        pass
