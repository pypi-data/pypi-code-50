''' bulk downloads ENRs and converts to dataframes/csvs/etc

to run: python bulk_downloader.py --start_year YYYY --end_year YYYY num_threads = 16
'''

import argparse
import datetime
import logging
import sys
from queue import Queue
from threading import Thread

import pandas as pd

import nrc_scrape
import nrc_scrape.main
from nrc_scrape import main
from nrc_scrape.main import EventNotificationReport, HTTPError, headers


def urls2list(urls: dict):
    '''generates a list of EventNotificationReport objects from a list of urls'''
    urls_l = []
    for year, months in urls.items():
        for month, murls in months.items():
            for url in murls:
                urls_l.append(url)
    return urls_l


class EnrDownloadWorker(Thread):
    ''' worker thread to get event report url'''
    def __init__(self, url_queue, enr_queue):
        Thread.__init__(self)
        self.url_queue = url_queue
        self.enr_queue = enr_queue

    def run(self):
        while True:
            url = self.url_queue.get()
            try:
                print(url)
                enr = EventNotificationReport.from_url(url, headers)
                self.enr_queue.put(enr)
                sl.info(enr)
            except:
                el.info(url)
            finally:
                self.url_queue.task_done()


def run(year):
    ''' spins up worker threads, downloads and parses a year of ENRs into queue, returns queue'''
    urls: dict = main.generate_nrc_event_report_urls(year, year)

    urls = urls2list(urls)
    print(len(urls))

    enr_urls_queue = Queue()
    enr_queue = Queue()

    for worker_num in range(16):
        worker = EnrDownloadWorker(enr_urls_queue, enr_queue)
        worker.daemon = True
        worker.start()

    for url in urls:
        enr_urls_queue.put(url)

    enr_urls_queue.join()

    return enr_queue


if __name__ == "__main__":
    ''' bulk downloads ENRs and converts to dataframes/csvs/etc'''
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_year', type=int,
                        help="First year to download event reports.", default=2004)
    parser.add_argument('--threads', type=int,
                        help="Number of concurrent download threads.", default=16)
    parser.add_argument('--end_year', type=int, help="Last year to download event reports.",
                        default=datetime.datetime.now().year)
    args = parser.parse_args()

    sl = logging.getLogger('success_log')
    el = logging.getLogger('error_log')
    fl = logging.getLogger('fof_log')

    for year in range(args.start_year, args.end_year+1):
        q = run(year)
        enrs = []
        while not q.empty():
            enrs.append(q.get())

        enr_dfs = []
        for enr in enrs:
            try:
                enr_df = enr.to_dataframe()
                enr_dfs.append(enr_df)
            except:
                pass

        df = pd.concat(enr_dfs)
        df.to_csv(str(year) + '.csv')
