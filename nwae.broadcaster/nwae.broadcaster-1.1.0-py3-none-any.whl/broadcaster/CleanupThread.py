# -*- coding: utf-8 -*-

import time
import threading
from nwae.utils.Log import Log
from inspect import getframeinfo, currentframe
from nwae.utils.Cleanup import Cleanup


class CleanupThread(threading.Thread):

    def __init__(
            self,
            cleanup_folder,
            files_regex,
            max_age_secs
    ):
        super().__init__()

        self.cleanup_folder = cleanup_folder
        self.files_regex = files_regex
        self.max_age_secs = max_age_secs

        self.cleanup = Cleanup(
            folder = self.cleanup_folder,
            regex  = self.files_regex,
            max_age_secs = self.max_age_secs
        )
        return

    def run(self):
        Log.important(
            str(self.__class__) + ' ' + str(getframeinfo(currentframe()).lineno)
            + ': Starting Cleanup Thread for folder "' + str(self.cleanup_folder)
            + '", regex "' + str(self.files_regex)
            + '", max age secs = ' + str(self.max_age_secs) + '.'
        )
        while True:
            self.cleanup.remove_old_files()

            time.sleep(10)


if __name__ == '__main__':
    obj = CleanupThread(
        cleanup_folder = '/usr/local/git/nwae/nwae.broadcaster/app.data/feed.cache',
        files_regex = '.*.cache$',
        max_age_secs = 20
    )
    obj.start()
