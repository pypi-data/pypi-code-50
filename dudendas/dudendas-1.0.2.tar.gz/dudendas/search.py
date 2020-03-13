import logging
import re

from urllib.parse import urlparse, parse_qs

from .network import build_soup, load_page, load_pages
from .word import DudenWord

logger = logging.getLogger("dudendas")


class DudenSearch(object):
    HREF_PATTERN = re.compile(r"https://www\.duden\.de/rechtschreibung/.*")
    query = "https://www.duden.de/suchen/dudenonline/{keyword}?page={page}"

    def __init__(self, keyword):
        self.keyword = keyword
        self.words = set()
        self.results = set()
        self.page_count = self._get_page_count()

    def __repr__(self):
        fmt = "<DudenSearch '{}'>"
        return fmt.format(self.keyword)

    def parse_results(self):
        urls = self._build_urls(self.page_count)

        msg = 'Start parsing {} results.'
        logger.debug(msg.format(len(urls)))

        for k, result in enumerate(load_pages(urls)):
            url, content = result

            soup = build_soup(content)

            try:
                logger.info("Loading page [%d/%d].", k + 1, self.page_count + 1)
                links = soup.find_all("a", href=self.HREF_PATTERN)

                msg = 'Found {} matches on page {}.'
                logger.debug(msg.format(len(links), k + 1))

                for l in links:
                    href = l["href"]
                    self.results.add(href)
            except Exception as e:
                logger.warning("Caught %s for page %d.", type(e).__name__, k + 1)

        return self.results

    def parse_words(self, group=None):
        msg = 'Start parsing {} words.'
        logger.debug(msg.format(len(self.results)))

        for k, result in enumerate(load_pages(self.results)):
            url, content = result

            soup = build_soup(content)
            name = DudenSearch._name_from_href(url)

            logger.info("Parsing %s [%d/%d].", name, k + 1, len(self.results))

            try:
                word = DudenWord(name, url, soup)
                if word.belongs_to(group):
                    self.words.add(word)
            except Exception as e:
                logger.warning("Caught %s for word '%s'.", type(e).__name__, name)

        return self.words

    def _build_urls(self, page_count):
        r = range(0, self.page_count + 1)
        urls = [self.query.format(keyword=self.keyword, page=p) for p in r]
        return urls

    def _get_page_count(self):
        soup = self._load_page(0)

        pager_last = soup.find("span", "pager-last").a

        if pager_last is None:
            pages = 1
        else:
            tmp_url = pager_last["href"]
            query_raw = urlparse(tmp_url).query
            query = parse_qs(query_raw)
            pages = int(query["page"][0])

        msg = 'Page count is {}.'
        logger.debug(msg.format(pages))

        return pages

    def _load_page(self, page):
        url = self.query.format(keyword=self.keyword, page=page)

        msg = "Loading page '{}'."
        logger.debug(msg.format(url))

        return load_page(url)

    @staticmethod
    def _name_from_href(href):
        path = urlparse(href).path
        word = path.split("/")[-1]
        return word
