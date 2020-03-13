import logging
import re

from .exception import DudendasException
from .util import decompose_all, parse_list, flatten_list

logger = logging.getLogger("dudendas")


class DudenWord(object):
    def __init__(self, word, url, soup):
        self.word = word
        self.url = url

        self.title = self._get_title(soup)
        self.meaning = self._get_meaning(soup)
        self._block = soup.find(id="block-system-main")

        if self._block is None:
            msg = "Cannot find the main section for '{}'."
            raise DudendasException(msg.format(self.word))

    def __repr__(self):
        fmt = "<DudenWord '{}'>"
        return fmt.format(self.word)

    def __eq__(self, other):
        return self.word == other.word

    def __hash__(self):
        return hash(self.word)

    def belongs_to(self, group):
        for s in self._block.find_all("strong"):
            if s.string is not None and group in s.string:
                return True

        for m in flatten_list(self.meaning):
            if re.search(r"\(.*" + group + r".*\)", m):
                return True
            elif re.search(group + " für", m):
                return True

        logger.debug("Word '%s' does not belong to group '%s'.", self.word, group)

        return False

    def serialize(self):
        meaning = flatten_list(self.meaning)
        meaning = "\n".join(meaning)

        return dict(word=self.word,
                    title=self.title,
                    meaning=meaning,
                    url=self.url)

    def _get_title(self, soup):
        h1 = soup.h1.string
        return h1.strip()

    def _get_meaning(self, soup):
        section = self._find_section(soup, "Bedeutungsübersicht")

        if section is None:
            return ""

        for name in ["header", "section", "figure"]:
            decompose_all(section, name)

        return [parse_list(section)]

    def _find_section(self, soup, title, approximate=False):
        for section in soup.find_all("section"):
            if section.h2:
                if section.h2.text == title:
                    return section
                elif approximate and title in section.h2.text:
                    return section

        return None
