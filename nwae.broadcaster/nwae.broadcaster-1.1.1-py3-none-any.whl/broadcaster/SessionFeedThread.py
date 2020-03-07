# -*- coding: utf-8 -*-

import threading
from nwae.utils.Log import Log
from inspect import currentframe, getframeinfo
from nwae.utils.ObjectPersistence import ObjectPersistence
from datetime import datetime
import nwae.utils.Profiling as prf
import os
import time


#
# Return session feed IDs from cache folder
# TODO Still not working
#
class SessionFeedThread(threading.Thread):

    def __init__(
            self,
            # We keep the session feeds in a file, not memory
            cache_file_path,
            lock_file_path,
            # Where all the feed resides
            feed_cache_folder,
            # Key to identify the unique key of the feed
            feed_id_key,
            # We put higher than the usual 5 mins
            timeout_secs = 30*60
    ):
        super().__init__()
        self.cache = ObjectPersistence(
            default_obj = {},
            obj_file_path = cache_file_path,
            lock_file_path = lock_file_path
        )
        self.feed_cache_folder = feed_cache_folder
        if not os.path.exists(self.feed_cache_folder):
            raise Exception(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Feed cache folder "' + str(self.feed_cache_folder)
                + '" does not exist!'
            )
        self.feed_id_key = feed_id_key

        self.timeout_secs = timeout_secs
        self.__mutex = threading.Lock()
        try:
            self.__cleanup_old_feeds()
        except Exception as ex:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                + ': Feed cleanup exception: ' + str(ex)
            )
        return

    def __sanity_check_feed(
            self,
            feed_obj
    ):
        if type(feed_obj) is not dict:
            errmsg = \
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno) \
                + ': Wrong feed object type "' + str(type(feed_obj)) + '". Expected dict type.'
            Log.error(errmsg)
            return False
        else:
            return True

    def __update_persistent_object(
            self,
            cache_obj,
            comment = None
    ):
        if not self.cache.update_persistent_object(new_obj=cache_obj):
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Error updating session cache: ' + str(comment)
            )
        else:
            Log.info(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Successfully updated session cache: ' + str(comment)
            )

    def __cleanup_old_feeds(self):
        cache_obj = self.cache.read_persistent_object()

        expired_feed_ids = []
        for feed_obj in cache_obj.values():
            feed_id = feed_obj[self.feed_id_key]
            last_updated = feed_obj.get_last_updated_time()
            dif_secs = prf.Profiling.get_time_dif(start=last_updated, stop=datetime.now(), decimals=1)
            if dif_secs > self.timeout_secs:
                Log.important(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ': Put feed ID "' + str(feed_id) + '", last updated "' + str(last_updated)
                    + '" for removal from session chats.'
                )
                expired_feed_ids.append(feed_id)
            else:
                Log.info(
                    str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                    + ' Feed ID "' + str(feed_id) + '" OK, last active time "' + str(last_updated)
                    + '" is within ' + str(dif_secs) + 's from current time.'
                )

        try:
            self.__mutex.acquire()
            for feed_id in expired_feed_ids:
                if feed_id in cache_obj.keys():
                    del cache_obj[feed_id]
                    Log.important(
                        str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                        + ': Deleted feed ID "' + str(feed_id) + '" from session chats.'
                    )
            self.__update_persistent_object(
                cache_obj = cache_obj,
                comment = "cleanup old feeds."
            )
        except Exception as ex:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Exception cleanup old feeds: ' + str(ex)
            )
        finally:
            self.__mutex.release()

    def add_new_feed(
            self,
            feed_obj
    ):
        if not self.__sanity_check_feed(feed_obj = feed_obj):
            return False

        feed_id = None
        try:
            self.__mutex.acquire()
            feed_id = feed_obj.get_chat_id()

            cache_obj = self.cache.read_persistent_object()
            cache_obj[feed_id] = feed_obj.get_chat_json(
                include_chat_history = False
            )
            self.__update_persistent_object(
                cache_obj = cache_obj,
                comment = 'adding feed "' + str(feed_id) + '"'
            )
        except Exception as ex:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Error adding feed "' + str(feed_id) + '" into session cache.'
            )
        finally:
            self.__mutex.release()

    def remove_feed(
            self,
            feed_obj
    ):
        if not self.__sanity_check_feed(feed_obj = feed_obj):
            return False

        # TODO Put this in separate thread
        self.__cleanup_old_feeds()

        feed_id = None
        try:
            self.__mutex.acquire()
            feed_id = feed_obj.get_chat_id()

            cache_obj = self.cache.read_persistent_object()

            if feed_id in cache_obj.keys():
                del cache_obj[feed_id]
                self.__update_persistent_object(
                    cache_obj = cache_obj,
                    comment = 'removing feed "' + str(feed_id) + '"'
                )
        except Exception as ex:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Error removing feed "' + str(feed_id) + '" from session cache.'
            )
        finally:
            self.__mutex.release()

    def to_json(
            self,
            # Return all if None
            bot_id = None,
            # Chat history is inaccurate and probably not updated
            include_chat_history = False
    ):
        cache_obj = self.cache.read_persistent_object()
        if type(cache_obj) is not dict:
            Log.error(
                str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
                + ': Wrong type for session cache object "' + str(type(cache_obj))
            )
            return None

        return_cache_obj = {}
        for chat_id in cache_obj.keys():
            chat_dict = cache_obj[chat_id]
            chat_bot_id = chat_dict[ch.Chat.JSON_BOTID]
            if ( bot_id is None ) or ( str(bot_id) == str(chat_bot_id) ):
                if not include_chat_history:
                    if ch.Chat.JSON_CHAT_HISTORY in chat_dict.keys():
                        del chat_dict[ch.Chat.JSON_CHAT_HISTORY]
                return_cache_obj[chat_id] = chat_dict

        return return_cache_obj

    def run(self):
        while True:
            time.sleep(10)


