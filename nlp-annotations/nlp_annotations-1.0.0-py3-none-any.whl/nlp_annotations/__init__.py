import typing as ty
import re


RP = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')


def markdown_links2entity_list(markdown_string: str) -> ty.Tuple:
    linkless_string = ""
    entities = []
    idx = 0
    for link in RP.finditer(markdown_string):
        word, entity = link.groups()[0], link.groups()[1]
        start, end = link.start(0), link.end(0)
        linkless_string += markdown_string[idx:start]
        word_idx = len(linkless_string)
        linkless_string += word
        idx = end
        entities.append((word_idx, word_idx + len(word), entity))  # Append to entities

    linkless_string += markdown_string[end:]  # Add the rest of the string
    return (linkless_string, {"entities": entities})


def entity_list2markdown_links(text: str, entities: ty.List) -> str:
    markdown_string = ""
    idx = 0
    for start, end, entity in entities:
        markdown_string += text[idx:start] + f"[{text[start:end]}]({entity})"
        idx = end
    markdown_string += text[idx:]
    return markdown_string
