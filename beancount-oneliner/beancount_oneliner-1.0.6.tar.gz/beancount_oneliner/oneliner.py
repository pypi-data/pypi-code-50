__author__ = 'Akuukis <akuukis@kalvis.lv'
__plugins__ = ['oneliner']

import sys, re

from beancount.core.amount import Amount, mul
from beancount.core import data
from beancount.core.position import Cost
from beancount.core.number import D
from beancount.core.data import EMPTY_SET
from .transform import txFromOneliner, isOneliner

RE_COST = re.compile(r"\{(.*)\}")
RE_PRICE = re.compile(r"\ \@(.*?)\*")
RE_TAG = re.compile(r"(?<=\s)(#)([A-Za-z0-9\-_/@.]+)")

def oneliner(entries, options_map, config):
    """
    Parse note oneliners into valid transactions. For example,
    ```beancount
    1999-12-31 note Assets:Cash "Income:Test -16.18 EUR * Description goes here *"
    ```
    """

    errors = []

    new_entries = []

    for entry in entries:
        if(isOneliner(entry)):
            try:
                entry = txFromOneliner(entry)
                new_entries.append(entry)
                # print(e)
            except:
                print('beancount_oneliner error:', entry, sys.exc_info())
        else:
            new_entries.append(entry)

    return new_entries, errors
