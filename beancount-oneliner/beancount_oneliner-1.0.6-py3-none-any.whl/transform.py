__author__ = 'Akuukis <akuukis@kalvis.lv'

import re

from beancount.core.amount import Amount, mul
from beancount.core import data
from beancount.core.position import Cost
from beancount.core.number import D
from beancount.core.data import EMPTY_SET

RE_COST = re.compile(r"\{(.*)\}")
RE_PRICE = re.compile(r"\ \@(.*?)\*")
RE_TAG = re.compile(r"(?<=\s)(#)([A-Za-z0-9\-_/@.]+)")

def prefixHash(string):
    return '#' + string

def prefixCarrot(string):
    return '^' + string

def onelinerFromTx(tx: data.Transaction, alignDotAt=90, alignAccountAt=0) -> data.Note:
    """
    Usage:
    ```
        # Given a transaction..
        tx_entry = data.Transaction(...)
        # Get a matching oneliner note.
        note_entry = onelinerFromTx(tx_entry)
    ```

    Assuming max account name length is 32, to acommodiate 6-digit numbers recommended alignDotAt is 90 (and alignAccountAt is 50).
    ```
    2020-01-02 note Assets:Cash                      "Expenses:Random                     123.45 EUR * ShopA | some stuff.. *"
    2020-01-02 note Assets:BankABC:Checking          "Expenses:Groceries                   43.21 EUR * ShopB | some groceries *"
    #                           |--------------------^                |----------------------^
    #                                       |--------^                   |-------------------^
    #                                (alignAccountAt = 50)                       (alignDotAt = 90)

    2020-01-02 note Assets:Cash "Expenses:Random                                          123.45 EUR * ShopA | some stuff.. *"
    2020-01-02 note Assets:BankABC:Checking "Expenses:Groceries                            43.21 EUR * ShopB | some groceries *"
    #                                            |-------------------------------------------^
    #                                                           |----------------------------^
    # (alignAccountAt = 0)                                                       (alignDotAt = 90)
    ```
    """

    tagString = ' '.join(list(map(prefixHash, tx.tags)))
    tagLinks = ' '.join(list(map(prefixCarrot, tx.links)))

    commentAccount = tx.postings[1].account
    commentRest = "{} * {} | {} {} {} *".format(tx.postings[1].units, tx.payee, tx.narration, tagString, tagLinks)

    preDotLen = len(str(tx.postings[1].units).split('.')[0])

    prefixLen = len('____-__-__ note ' + tx.postings[0].account + ' "')
    middleLen = len(tx.postings[1].account + ' ') + preDotLen
    pad = ' ' * max(1, (alignDotAt - prefixLen - middleLen - (max(0, alignAccountAt - prefixLen))))

    entry = data.Note(tx.meta, tx.date, tx.postings[0].account, commentAccount + pad + commentRest)

    return entry

def isOneliner(entry):
    return isinstance(entry, data.Note) and entry.comment[-1:] == "*"

def txFromOneliner(note: data.Note) -> data.Transaction:
        comment = note.comment
        k = None
        maybe_cost = RE_COST.findall(comment)
        if len(maybe_cost) > 0:
            amount = maybe_cost[0].split()[0]
            currency = maybe_cost[0].split()[1]
            cost = Cost(D(amount), currency, None, None)
            k = mul(cost, D(-1))
            comment = RE_COST.sub('', comment)
        else:
            cost = None

        maybe_price = RE_PRICE.findall(comment)
        if len(maybe_price) > 0:
            price = Amount.from_string(maybe_price[0])
            k = k or mul(price, D(-1))
            comment = RE_PRICE.sub('', comment)
        else:
            price = None

        comment_tuple = comment.split()
        other_account = comment_tuple[0]
        units = Amount.from_string(' '.join(comment_tuple[1:3]))
        flag = comment_tuple[3]
        narration_tmp = ' '.join(comment_tuple[4:-1])
        tags = {'NoteToTx'}
        for tag in RE_TAG.findall(narration_tmp):
            tags.add( tag[1] )
        narration = RE_TAG.sub('', narration_tmp).rstrip()

        k = k or Amount(D(-1), units.currency)

        # print(type(cost), cost, type(price), price, type(units), units, k, comment)
        p1 = data.Posting(
            account=other_account,
            units=units,
            cost=cost,
            price=price,
            flag=None,
            meta={'filename': note.meta['filename'], 'lineno': note.meta['lineno']}
        )
        p2 = data.Posting(
            account=note.account,
            units=mul(k, units.number),
            cost=cost,
            price=None,
            flag=None,
            meta={'filename': note.meta['filename'], 'lineno': note.meta['lineno']}
        )
        tx = data.Transaction(
            date=note.date,
            flag=flag,
            payee=None,  # TODO
            narration=narration,
            tags=tags,  # TODO
            links=EMPTY_SET,  # TODO
            postings=[p1, p2],
            meta=note.meta
        )

        return tx
