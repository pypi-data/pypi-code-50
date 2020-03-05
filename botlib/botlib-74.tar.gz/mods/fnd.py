# BOTLIB - Framework to program bots.
#
#

import lo
import os
import time

def find(event):
    if not event.args:
        wd = os.path.join(lo.workdir, "store", "")
        lo.cdir(wd)
        fns = os.listdir(wd)
        fns = sorted({x for x in fns})
        if fns:
            event.reply("|".join(fns))
        return
    if not len(event.args) > 1:
        event.reply("find <type> <match>")
        return
    otype = event.args[0]
    match = event.args[1]
    try:
        args = event.args[2:]
    except ValueError:
        args = None
    nr = -1
    db = lo.Db()
    for o in db.find_value(otype, match):
        nr += 1
        event.display(o, str(nr), args)
