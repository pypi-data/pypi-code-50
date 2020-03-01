"""Code runner components."""


import re
from typing import Iterator

import bs4


def findall(markdown: str, query: str) -> Iterator[str]:
    """Find all matching code blocks.

    Args:
        markdown: Text to parse.

    Return:
        Text from code blocks.
    """

    regex = re.compile(
        """
        \\s+```javascript\\s+         # Find JavaScript code block start
        (.*?)                         # Capture JavaScript code
        \\s+```\\s+                       # Find JavaScript code block end
        """,
        re.DOTALL | re.MULTILINE | re.VERBOSE,
    )

    soup = bs4.BeautifulSoup(markdown, "html.parser")
    for match in soup.select(query):
        yield from regex.findall(match.text)


def runner(markdown: str, selector: str) -> str:
    """Pulls code from.

    Args:
        markdown:
        selector:

    Return:
        Markdown text with generated scripts.
    """

    element = "\n<script>\n{}\n</script>"
    listener = 'window.addEventListener("load", () => {{\n{}\n}});'
    script = element.format(listener)

    for code in findall(markdown, selector):
        markdown += script.format(code)

    return markdown
