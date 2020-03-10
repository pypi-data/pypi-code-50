import urllib.parse
from dataclasses import dataclass, field


def _format_to_pythontutor_link(code):
    link = "".join(
        [
            "http://www.pythontutor.com/visualize.html#code=",
            urllib.parse.quote(code),
            "&cumulative=false",
            "&curInstr=0",
            "&heapPrimitives=nevernest",
            "&mode=display",
            "&origin=opt-frontend.js",
            "&py=3&rawInputLstJSON=%5B%5D&textReferences=false",
        ]
    )

    return link


def _wrap_list_to_code(l):
    return "\n".join(
        ["```python", "\n".join(map(lambda s: s.strip("\n"), l)), "```"]
    )


@dataclass
class Question:

    answer: str
    answer_value: str
    _code_lines: list
    _explanation_lines: list
    alternates: set = field(default_factory=lambda: set())

    @property
    def pythontutor_link(self):
        return _format_to_pythontutor_link("".join(self._code_lines))

    @property
    def md_code(self):
        return _wrap_list_to_code(self._code_lines)

    @property
    def explanation(self):
        return _wrap_list_to_code(self._explanation_lines)
