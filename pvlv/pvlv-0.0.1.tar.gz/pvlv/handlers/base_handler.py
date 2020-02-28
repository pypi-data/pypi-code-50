from pvlv.pvlv import BotInterface

from pvlv.static.configurations import logger, LOGGING_CHAT
from pvlv_database import Database, StatsUpdater
from pvlv_img_builder.level_up_card import DrawLevelUpCard
from pvlv.handlers.level_up.level_up_reply import user_field, text_description
from pvlv.handlers.antispam.antispam_reply import spam_detected_reply
from pvlv_commando import (
    CommandNotFound,
    CommandExecutionFail,
    ArgVoidNotAllowed,
    ParamNotFound,
    MaxHourlyUses,
    MaxDailyUses,
)
from pvlv_commando import Commando

com = Commando()  # load all the the commands in the commands dir


class BaseHandler(object):
    """
    Middle point to prepare data that have to be saved to the database
    This is an interface between the platform-wrapper and the other modules

    This Handler will handle the operations on the text.
     - stats updating
     - command reading
     - text interactions
    """
    def __init__(self, bot_interface):
        self.bot: BotInterface = bot_interface

        self.db = Database(self.bot.guild_id, self.bot.user_id)  # load database

        # Update the stats (this are standard for all type of messages)
        # The others stats must be set in the specific handler
        self.stats_updater = StatsUpdater(self.db)
        self.stats_updater.timestamp(self.bot.timestamp)
        self.stats_updater.username(self.bot.username)
        self.stats_updater.guild_name(self.bot.guild_name)

    @property
    def is_bot_disabled(self):
        """
        if the guild is disabled,
        this means that the bot will ignore all the messages from that guild
        :return: the bot disable status
        """
        return self.db.guild.bot_disabled

    def check_spam(self):
        if self.stats_updater.is_spam:
            self.bot.reply_text(spam_detected_reply(self.db.guild.languages[0]))

    def check_level_up(self):
        """
        Check if the user has reached the xp to level up.
        If yes, send the level up chard in the same chat.
        The level up card has text, so in must be formatted based on the guild language
        """
        # check if the bot is paused in that guild
        if self.db.guild.bot_paused:
            return

        if self.stats_updater.is_level_up:
            data = {
                'level': self.db.user.guild.xp.level,
                'bold_text': user_field(self.db.guild.languages[0], self.bot.username),
                'text': text_description(self.db.guild.languages[0], self.db.user.guild.xp.level),
            }
            d = DrawLevelUpCard(data)
            d.draw_level_up()

            # Have level_up notifications enabled? then send in te chat
            if self.db.guild.level_up_notification:
                self.bot.reply_photo(d.get_image())
            # else send it directly to the user
            else:
                self.bot.send_photo(self.bot.user_id, d.get_image())

    def check_commands(self, text):
        """
        Check if the text is a command.
        If yes execute it
        Here will be check:
        - the prefix handling (based on guild)
        - user permission to run the command
        - error handling, message error sending to log chat

        :param text: the text where search the command
        """

        if text.startswith('.'):
            log_message = 'User {} in {} sent "{}"'.format(
                    self.bot.username,
                    self.bot.guild_name,
                    text,
            )
            logger.info(log_message)

            try:
                # text without the command invocation word, and the language of the command
                command = com.find_command(text[1:], self.db.guild.languages[0], self.db.user.guild.permissions)

                user_command_use = self.db.user.guild.commands.command(command)
                if user_command_use:
                    com.hourly_executions = user_command_use.log_by_hour[0][1]
                    com.daily_executions = user_command_use.log_by_day[0][1]

                # Here you have to pass the bot object and the update obj that will be used
                out = com.run_command(self.bot)
                self.db.user.guild.commands.increment_command_interactions(command, self.bot.timestamp)

                if out:
                    # must be sent with parse mode enabled
                    self.bot.reply_text(out, parse_mode=True)

            except CommandExecutionFail as exc:
                # error of the command, send to a log chat
                self.bot.reply_text(str(exc))  # the exception to send in chat
                logger.error(exc.error_report)
                self.bot.send_text(LOGGING_CHAT, '{}\n\n{}'.format(log_message, exc.error_report))

            except CommandNotFound as exc:
                self.bot.reply_text(str(exc))
                self.bot.send_text(LOGGING_CHAT, '{}\nCommand Not Found'.format(log_message))

            except ArgVoidNotAllowed as exc:
                self.bot.reply_text(str(exc))
                self.bot.send_text(LOGGING_CHAT, '{}\nArg Void Not Allowed'.format(log_message))

            except ParamNotFound as exc:
                self.bot.reply_text(str(exc))
                self.bot.send_text(LOGGING_CHAT, '{}\nParam Not Found'.format(log_message))

            except MaxHourlyUses as exc:
                self.bot.reply_text(str(exc))
                self.bot.send_text(LOGGING_CHAT, '{}\nUser has exceed MaxHourlyUses'.format(log_message))

            except MaxDailyUses as exc:
                self.bot.reply_text(str(exc))
                self.bot.send_text(LOGGING_CHAT, '{}\nUser has exceed MaxDailyUses'.format(log_message))

            self.bot.send_text(LOGGING_CHAT, '{}\nCommand Executed'.format(log_message))

            return True
        return False
