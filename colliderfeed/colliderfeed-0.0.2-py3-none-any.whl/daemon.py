from colliderfeed.collider_feed_config_private import COLLIDER_FEED_CONFIG as config
import asyncio, aiohttp, json, requests, schedule, time
from retrying import retry
from contexttimer import Timer


async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        return await response.text()

async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def fetch_prices(symbols):
    urls = [ config["template_url"].replace("SYMBOL",symbol) for symbol in symbols ]
    async with aiohttp.ClientSession() as session:
        results = await fetch_all(session, urls)
    prices = [json.loads(r).get('Global Quote')['05. price'] for r in results]
    return prices

def retry_if_result_none(result):
    """Return True if we should retry (in this case when result is None), False otherwise"""
    return result is None

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000,retry_on_result=retry_if_result_none)
def collider_prices(symbols):
    """ Get prices from market data feed """
    prices =  asyncio.run( fetch_prices(symbols=symbols ) )
    if prices is None:
        raise Exception("Feed may be down")
    return prices

def set_or_touch( names, write_key, budgets, values=None, touch=True):
    """ Use web microprediction API to set or touch names """
    base_url = "http://www.3za.org/multi/"
    request_data = {"names": ",".join(names), "write_key": write_key,
                    "budgets": ",".join([str(b) for b in budgets])}
    if touch:
        res = requests.put(base_url,data=request_data)
    else:
        if values:
            request_data.update( {"values":",".join( [str(v) for v in values])}  )
            res = requests.put(base_url, data=request_data)
        else:
            return None
    return res.status_code==200

prev_prices = None

def minutely_feed_task():
    """ Modify feed of price changes or at least keep it warm """
    global prev_prices, config
    with Timer() as t_get:
        prices = collider_prices(symbols=config["symbols"])
    print( str(t_get.elapsed)+'s getting data.')
    authority = dict([ (k,v) for k,v in config.items() if k in ['names','write_key','budgets'] ] )
    if prev_prices is None or prices is None:
        set_or_touch(touch=True,**authority )
        if prev_prices is None:
            prev_prices = [ p for p in prices ]
    else:
        price_changes = [ float(p)-float(pp) for p,pp in zip(prices,prev_prices) ]
        stale = all( [ abs(pc)<1e-5 for pc in price_changes ] )
        if stale:
            set_or_touch(touch=True, **authority)
        else:
            with Timer() as t_put:
                set_or_touch(touch=False, values=price_changes, **authority )
            print(str(t_put.elapsed)+ 's putting data.')
            prev_prices = [ p for p in prices ]


if __name__=="__main__":
    schedule.every(1).minutes.do(minutely_feed_task)
    while True:
        schedule.run_pending()
        time.sleep(1)

