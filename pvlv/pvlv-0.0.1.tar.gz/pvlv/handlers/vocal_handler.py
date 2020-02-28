from threading import Thread
from pvlv.handlers.base_handler import BaseHandler
from pvlv.handlers.speech_to_text.speech_to_text import speech_to_text


class VocalHandler(BaseHandler):
    """
    It will handle the operations on the text.
    """
    def __init__(self, bot_interface):
        super().__init__(bot_interface)

    def handle(self, file, duration):

        # do fast stuff
        self.stats_updater.update_vocal(duration)  # update stats
        self.check_level_up()

        # if the bot is paused don't do stt conversions.
        if not self.db.guild.bot_paused:
            # run the speech to text on another thread, cause it's time consuming operation
            t = Thread(target=speech_to_text, args=(self.bot, file, self.bot.guild_id, self.db.guild.languages[0]))
            t.start()
