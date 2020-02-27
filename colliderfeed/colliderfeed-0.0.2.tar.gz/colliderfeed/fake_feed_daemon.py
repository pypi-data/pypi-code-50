from colliderfeed.collider_feed_config_private import COLLIDER_FEED_CONFIG as config
import requests, schedule, time
from contexttimer import Timer
import numpy as np
from .daemon import set_or_touch

# Will overwrite real data if symbols aren't changed !!!!

def fake_collider_prices(symbols):
    """ Fake """
    prices =  list(np.exp(np.random.randn(len(symbols))))
    if prices is None:
        raise Exception("Feed may be down")
    return prices

prev_prices = None
def minutely_fake_feed_task():
    """ Modify feed of price changes or at least keep it warm """
    global prev_prices, config
    with Timer() as t_get:
        prices = fake_collider_prices(symbols=config["symbols"])
    print( str(t_get.elapsed)+'s getting data.')
    authority = dict([ (k,v) for k,v in config.items() if k in ['names','write_key','budgets'] ] )
    if prev_prices is None or prices is None:
        set_or_touch(touch=True,**authority )
        if prev_prices is None:
            prev_prices = [ p for p in prices ]
    else:
        price_changes = [ p-pp for p,pp in zip(prices,prev_prices) ]
        stale = all( [ abs(pc)<1e-5 for pc in price_changes ] )
        if stale:
            set_or_touch(touch=True, **authority)
        else:
            with Timer() as t_put:
                set_or_touch(touch=False, values=price_changes, **authority )
            print(str(t_put.elapsed)+ 's putting data.')
            prev_prices = [ p for p in prices ]


if __name__=="__main__":
    schedule.every(5).seconds.do(minutely_fake_feed_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

