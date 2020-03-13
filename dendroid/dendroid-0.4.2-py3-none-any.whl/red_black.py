from reprlib import recursive_repr
from typing import (Iterable,
                    Optional,
                    Tuple,
                    Union)

from reprit.base import generate_repr

from .binary import (NIL,
                     Node as _Node,
                     TreeBase,
                     _to_unique_sorted_items,
                     _to_unique_sorted_values)
from .hints import (Domain,
                    Sortable,
                    SortingKey)
from .utils import (_dereference_maybe,
                    _maybe_weakref,
                    to_balanced_tree_height)


class Node(_Node):
    is_black = False  # type: bool
    parent = None  # type: Optional['Node']


class SimpleNode(Node):
    slots = ('_value', 'is_black', '_parent', '_left', '_right')

    def __init__(self, value: Domain,
                 *,
                 is_black: bool,
                 parent: Optional['SimpleNode'] = None,
                 left: Union[NIL, 'SimpleNode'] = NIL,
                 right: Union[NIL, 'SimpleNode'] = NIL) -> None:
        self._value = value
        self.is_black = is_black
        self.parent = parent
        self.left = left
        self.right = right

    __repr__ = recursive_repr()(generate_repr(__init__))

    State = Tuple[Domain, bool, Optional['SimpleNode'],
                  Union[NIL, 'SimpleNode'], Union[NIL, 'SimpleNode']]

    def __getstate__(self) -> State:
        return self._value, self.is_black, self.parent, self._left, self._right

    def __setstate__(self, state: State) -> None:
        (self._value, self.is_black,
         self.parent, self._left, self._right) = state

    @property
    def value(self) -> Domain:
        return self._value

    @property
    def key(self) -> Sortable:
        return self._value

    @property
    def parent(self) -> Optional['SimpleNode']:
        return _dereference_maybe(self._parent)

    @parent.setter
    def parent(self, node: Optional['SimpleNode']) -> None:
        self._parent = _maybe_weakref(node)

    @property
    def left(self) -> Union[NIL, 'SimpleNode']:
        return self._left

    @left.setter
    def left(self, node: Union[NIL, 'SimpleNode']) -> None:
        self._left = node
        _set_parent(node, self)

    @property
    def right(self) -> Union[NIL, 'SimpleNode']:
        return self._right

    @right.setter
    def right(self, node: Union[NIL, 'SimpleNode']) -> None:
        self._right = node
        _set_parent(node, self)


class ComplexNode(Node):
    slots = ('_key', '_value', 'is_black', '_parent', '_left', '_right')

    def __init__(self, key: Sortable, value: Domain,
                 *,
                 is_black: bool,
                 parent: Optional['ComplexNode'] = None,
                 left: Union[NIL, 'ComplexNode'] = NIL,
                 right: Union[NIL, 'ComplexNode'] = NIL) -> None:
        self._value = value
        self._key = key
        self.is_black = is_black
        self.parent = parent
        self.left = left
        self.right = right

    __repr__ = recursive_repr()(generate_repr(__init__))

    @property
    def value(self) -> Domain:
        return self._value

    @property
    def key(self) -> Sortable:
        return self._key

    @property
    def parent(self) -> Optional['ComplexNode']:
        return _dereference_maybe(self._parent)

    @parent.setter
    def parent(self, node: Optional['ComplexNode']) -> None:
        self._parent = _maybe_weakref(node)

    @property
    def left(self) -> Union[NIL, 'ComplexNode']:
        return self._left

    @left.setter
    def left(self, node: Union[NIL, 'ComplexNode']) -> None:
        self._left = node
        _set_parent(node, self)

    @property
    def right(self) -> Union[NIL, 'ComplexNode']:
        return self._right

    @right.setter
    def right(self, node: Union[NIL, 'ComplexNode']) -> None:
        self._right = node
        _set_parent(node, self)

    State = Tuple[Sortable, Domain, bool, Optional['ComplexNode'],
                  Union[NIL, 'ComplexNode'], Union[NIL, 'ComplexNode']]

    def __getstate__(self) -> State:
        return (self._key, self._value, self.is_black,
                self.parent, self._left, self._right)

    def __setstate__(self, state: State) -> None:
        (self._key, self._value, self.is_black,
         self.parent, self._left, self._right) = state


def _set_parent(node: Union[NIL, Node], parent: Optional[Node]) -> None:
    if node is not NIL:
        node.parent = parent


def _set_black(maybe_node: Optional[Node]) -> None:
    if maybe_node is not None:
        maybe_node.is_black = True


def _is_left_child(node: Node) -> bool:
    parent = node.parent
    return parent is not None and parent.left is node


def _is_node_black(node: Union[NIL, Node]) -> bool:
    return node is NIL or node.is_black


class Tree(TreeBase[Domain]):
    def __init__(self, root: Union[NIL, Node],
                 *,
                 key: Optional[SortingKey] = None) -> None:
        self._root = root
        self._key = key

    @property
    def root(self) -> Union[NIL, Node]:
        return self._root

    @property
    def key(self) -> Optional[SortingKey]:
        return self._key

    @classmethod
    def from_iterable(cls, _values: Iterable[Domain],
                      *,
                      key: Optional[SortingKey] = None) -> 'Tree[Domain]':
        values = list(_values)
        if not values:
            root = NIL
        elif key is None:
            values = _to_unique_sorted_values(values)
            height = to_balanced_tree_height(len(values))

            def to_node(start_index: int, end_index: int,
                        depth: int) -> SimpleNode:
                middle_index = (start_index + end_index) // 2
                return SimpleNode(values[middle_index],
                                  is_black=depth != height,
                                  left=(to_node(start_index, middle_index,
                                                depth + 1)
                                        if middle_index > start_index
                                        else NIL),
                                  right=(to_node(middle_index + 1, end_index,
                                                 depth + 1)
                                         if middle_index < end_index - 1
                                         else NIL))

            root = to_node(0, len(values), 0)
            root.is_black = True
        else:
            items = _to_unique_sorted_items(values, key)
            height = to_balanced_tree_height(len(items))

            def to_node(start_index: int, end_index: int, depth: int
                        ) -> ComplexNode:
                middle_index = (start_index + end_index) // 2
                return ComplexNode(*items[middle_index],
                                   is_black=depth != height,
                                   left=(to_node(start_index, middle_index,
                                                 depth + 1)
                                         if middle_index > start_index
                                         else NIL),
                                   right=(to_node(middle_index + 1, end_index,
                                                  depth + 1)
                                          if middle_index < end_index - 1
                                          else NIL))

            root = to_node(0, len(items), 0)
            root.is_black = True
        return cls(root,
                   key=key)

    def add(self, value: Domain) -> None:
        parent = self._root
        if parent is NIL:
            self._root = self._make_node(value,
                                         is_black=True)
            return
        key = self._to_key(value)
        while True:
            if key < parent.key:
                if parent.left is NIL:
                    node = self._make_node(value,
                                           is_black=False)
                    parent.left = node
                    break
                else:
                    parent = parent.left
            elif parent.key < key:
                if parent.right is NIL:
                    node = self._make_node(value,
                                           is_black=False)
                    parent.right = node
                    break
                else:
                    parent = parent.right
            else:
                return
        self._restore(node)

    def discard(self, value: Domain) -> None:
        try:
            node = self._search_node(value)
        except ValueError:
            return
        else:
            self._remove_node(node)

    def popmax(self) -> Domain:
        node = self.root
        if node is None:
            raise KeyError
        while node.right is not NIL:
            node = node.right
        self._remove_node(node)
        return node.value

    def popmin(self) -> Domain:
        node = self.root
        if node is None:
            raise KeyError
        while node.left is not NIL:
            node = node.left
        self._remove_node(node)
        return node.value

    def clear(self) -> None:
        self._root = NIL

    def _make_node(self, value: Domain,
                   *,
                   is_black: bool) -> Node:
        if self._key is None:
            return SimpleNode(value,
                              is_black=is_black)
        else:
            return ComplexNode(self._key(value), value,
                               is_black=is_black)

    def _restore(self, node: Node) -> None:
        while not _is_node_black(node.parent):
            parent = node.parent
            grandparent = parent.parent
            if parent is grandparent.left:
                uncle = grandparent.right
                if _is_node_black(uncle):
                    if node is parent.right:
                        self._rotate_left(parent)
                        node, parent = parent, node
                    parent.is_black, grandparent.is_black = True, False
                    self._rotate_right(grandparent)
                else:
                    parent.is_black = uncle.is_black = True
                    grandparent.is_black = False
                    node = grandparent
            else:
                uncle = grandparent.left
                if _is_node_black(uncle):
                    if node is parent.left:
                        self._rotate_right(parent)
                        node, parent = parent, node
                    parent.is_black, grandparent.is_black = True, False
                    self._rotate_left(grandparent)
                else:
                    parent.is_black = uncle.is_black = True
                    grandparent.is_black = False
                    node = grandparent
        self._root.is_black = True

    def _remove_node(self, node: Node) -> None:
        successor, is_node_black = node, node.is_black
        if successor.left is NIL:
            (successor_child, successor_child_parent,
             is_successor_child_left) = (successor.right, successor.parent,
                                         _is_left_child(successor))
            self._transplant(successor, successor_child)
        elif successor.right is NIL:
            (successor_child, successor_child_parent,
             is_successor_child_left) = (successor.left, successor.parent,
                                         _is_left_child(successor))
            self._transplant(successor, successor_child)
        else:
            successor = node.right
            while successor.left is not NIL:
                successor = successor.left
            is_node_black = successor.is_black
            successor_child, is_successor_child_left = successor.right, False
            if successor.parent is node:
                successor_child_parent = successor
            else:
                is_successor_child_left = _is_left_child(successor)
                successor_child_parent = successor.parent
                self._transplant(successor, successor.right)
                successor.right = node.right
            self._transplant(node, successor)
            successor.left, successor.left.parent = node.left, successor
            successor.is_black = node.is_black
        if is_node_black:
            self._remove_node_fixup(successor_child, successor_child_parent,
                                    is_successor_child_left)

    def _remove_node_fixup(self, node: Union[NIL, Node], parent: Node,
                           is_left_child: bool) -> None:
        while node is not self._root and _is_node_black(node):
            if is_left_child:
                sibling = parent.right
                if not _is_node_black(sibling):
                    sibling.is_black, parent.is_black = True, False
                    self._rotate_left(parent)
                    sibling = parent.right
                if (_is_node_black(sibling.left)
                        and _is_node_black(sibling.right)):
                    sibling.is_black = False
                    node, parent = parent, parent.parent
                    is_left_child = _is_left_child(node)
                else:
                    if _is_node_black(sibling.right):
                        sibling.left.is_black, sibling.is_black = True, False
                        self._rotate_right(sibling)
                        sibling = parent.right
                    sibling.is_black, parent.is_black = parent.is_black, True
                    _set_black(sibling.right)
                    self._rotate_left(parent)
                    node = self._root
            else:
                sibling = parent.left
                if not _is_node_black(sibling):
                    sibling.is_black, parent.is_black = True, False
                    self._rotate_right(parent)
                    sibling = parent.left
                if (_is_node_black(sibling.left)
                        and _is_node_black(sibling.right)):
                    sibling.is_black = False
                    node, parent = parent, parent.parent
                    is_left_child = _is_left_child(node)
                else:
                    if _is_node_black(sibling.left):
                        sibling.right.is_black, sibling.is_black = True, False
                        self._rotate_left(sibling)
                        sibling = parent.left
                    sibling.is_black, parent.is_black = parent.is_black, True
                    _set_black(sibling.left)
                    self._rotate_right(parent)
                    node = self._root
        _set_black(node)

    def _rotate_left(self, node: Node) -> None:
        replacement = node.right
        self._transplant(node, replacement)
        node.right, replacement.left = replacement.left, node

    def _rotate_right(self, node: Node) -> None:
        replacement = node.left
        self._transplant(node, replacement)
        node.left, replacement.right = replacement.right, node

    def _transplant(self, origin: Node, replacement: Union[NIL, Node]) -> None:
        parent = origin.parent
        if parent is None:
            self._root = replacement
            _set_parent(replacement, None)
        elif origin is parent.left:
            parent.left = replacement
        else:
            parent.right = replacement

    @staticmethod
    def _to_successor(node: Node) -> Node:
        if node.right is NIL:
            parent = node.parent
            while parent is not None and node is parent.right:
                node, parent = parent, parent.parent
            if parent is None:
                raise ValueError('Corresponds to a maximum node.')
            else:
                return parent
        else:
            result = node.right
            while result.left is not NIL:
                result = result.left
            return result

    @staticmethod
    def _to_predecessor(node: Node) -> Node:
        if node.left is NIL:
            parent = node.parent
            while parent is not None and node is parent.left:
                node, parent = parent, parent.parent
            if parent is None:
                raise ValueError('Corresponds to a minimum node.')
            else:
                return parent
        else:
            result = node.left
            while result.right is not NIL:
                result = result.right
            return result


def tree(*values: Domain, key: Optional[SortingKey] = None) -> Tree[Domain]:
    return Tree.from_iterable(values,
                              key=key)
