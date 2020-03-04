from __future__ import annotations

from typing import List, Optional


class SyntaxNode:

    def __init__(
            self,
            begin: int,
            end: int,
            rule: Optional[str]):
        self.begin = begin
        self.end = end
        self.rule = rule

    def to_dict(self) -> dict:
        raise NotImplementedError()


class ContainerNode(SyntaxNode):

    def __init__(
            self,
            begin: int,
            end: int,
            rule: Optional[str]):
        super().__init__(begin, end, rule)
        self.nodes: List[SyntaxNode] = []

    def to_dict(self) -> dict:
        return {
            'rule': self.rule,
            'nodes': [node.to_dict() for node in self.nodes],
        }


class TokenNode(SyntaxNode):

    def __init__(
            self,
            begin: int,
            end: int,
            rule: Optional[str],
            token: str):
        super().__init__(begin, end, rule)
        self.token = token

    def to_dict(self) -> dict:
        return {
            'rule': self.rule,
            'token': self.token,
        }
