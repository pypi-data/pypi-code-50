from typing import List

from gramat.expressions import Match
from gramat.lexing.nodes import SyntaxNode, TokenNode, ContainerNode
from gramat.parsing.source import Source


def generate_nodes(
        source: Source,
        matches: List[Match]) -> List[SyntaxNode]:
    nodes = []

    last_pos = fill_nodes(source, matches, nodes, 0)

    if last_pos < source.length:
        token = source.text[last_pos:source.length]

        nodes.append(TokenNode(last_pos, source.length, None, token))

    return nodes


def fill_nodes(
        source: Source,
        matches: List[Match],
        nodes: List[SyntaxNode],
        last_pos: int):
    for match in matches:
        if match.result:
            positive_count = sum(1 if m.result else 0 for m in match.items)

            if last_pos < match.begin:
                token = source.text[last_pos:match.begin]

                nodes.append(
                    TokenNode(last_pos, match.begin, None, token)
                )

                last_pos = match.begin

            if positive_count == 0:
                token = source.substring(match.begin, match.end)

                node = TokenNode(
                    match.begin, match.end, match.rule.name, token)

                last_pos = match.end
            else:
                node = ContainerNode(match.begin, match.end, match.rule.name)

                last_pos = fill_nodes(
                    source, match.items, node.nodes, last_pos)

                if last_pos < match.end:
                    token = source.text[last_pos:match.end]

                    node.nodes.append(
                        TokenNode(last_pos, match.end, None, token)
                    )

                    last_pos = match.end

            nodes.append(node)

    return last_pos
