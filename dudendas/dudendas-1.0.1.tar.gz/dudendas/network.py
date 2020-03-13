import aiohttp
import asyncio
import logging

from bs4 import BeautifulSoup
from urllib.request import urlopen

from .util import decompose_all

logger = logging.getLogger("dudendas")


def build_soup(page):
    page = page.replace("\u00ad", "")
    soup = BeautifulSoup(page, "html.parser")
    main = soup.find("main", id="content")
    decompose_all(main, "script")

    return main


def load_page(url):
    with urlopen(url) as page:
        page = page.read()

    soup = build_soup(page.decode("UTF-8"))

    return soup


async def _fetch_url(session, url, retries=5):
    content = None

    for i in range(retries):
        try:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()

        except aiohttp.ClientResponseError:
            msg = "Could not fetch '%s' [%d/%d]."
            logger.debug(msg, url, i + 1, retries)
            continue

        encoding = response.charset if response.charset else "ISO-8859-1"
        content = content.decode(encoding)
        break

    if content is None:
        msg = "Could not retrieve '{}'."
        logger.warning(msg.format(url))

    return url, content


async def _load_pages(urls, limit):
    def init_task(session, url):
        task = _fetch_url(session, url)
        return task

    connector = aiohttp.TCPConnector(limit=limit)

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [init_task(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    dl_successful = results.count(True)
    dl_rate = dl_successful / float(len(results))
    msg = "total: {}, successful: {}, rate: {}"
    logger.info(msg.format(len(results), dl_successful, dl_rate))

    return results


def load_pages(urls, limit=100):
    msg = "Downloading {} files."
    logger.info(msg.format(len(urls)))

    loop = asyncio.get_event_loop()
    func = _load_pages(urls, limit=limit)
    contents = loop.run_until_complete(func)

    return contents
