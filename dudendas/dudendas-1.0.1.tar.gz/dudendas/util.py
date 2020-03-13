import logging
import re

logger = logging.getLogger("dudendas")


def decompose_all(obj, name):
    for item in obj.find_all(name):
        item.decompose()


def parse_list(root):
    if root.name in ["ul", "ol"]:
        list_ = root
    else:
        list_ = root.ol or root.ul

    if list_ is not None:
        items = list_.find_all("li", recursive=False)
        return [parse_list(i) for i in items]
    else:
        text = root.get_text()
        return textify(text)


def textify(s):
    s = re.sub(r"\([a-z0-9][a-z]?\)", "", s)
    s = re.sub(r"\s{2,}", " ", s)
    s = s.strip()

    return s


def flatten_list(root):
    items = list()

    for item in root:
        if type(item) is list:
            items.extend(flatten_list(item))
        else:
            items.append(item)

    return items
