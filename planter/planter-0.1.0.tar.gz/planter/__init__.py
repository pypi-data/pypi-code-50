"""
MIT License

Copyright (c) 2020 williamfzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__PROJECT_NAME__ = r"planter"
__AUTHOR__ = r"williamfzc"
__AUTHOR_EMAIL__ = r"fengzc@vip.qq.com"
__LICENSE__ = r"MIT"
__URL__ = r"https://github.com/williamfzc/planter"
__VERSION__ = r"0.1.0"
__DESCRIPTION__ = r"compile dict (json/yaml/toml/everything) to tree"


import typing
import queue


class Node(object):
    def __init__(self, name: str, parent_name: str, depth: int, *_, **__):
        self.name: str = name
        self.parent_name: str = parent_name
        self.depth: int = depth

        self.sub_nodes: typing.List[Node] = []


class Compiler(object):
    NODE_KLS: typing.Type[Node] = Node
    ROOT_NODE_NAME: str = "root"

    def compile(self, data: dict) -> Node:
        def _compile(
            cur_data: dict, depth: int, cur_name: str, parent_name: str = None
        ) -> Node:
            cur_node = self.NODE_KLS(cur_name, parent_name, depth)
            for k, v in cur_data.items():
                # node
                if isinstance(v, dict):
                    sub_node = _compile(v, depth + 1, k, cur_name)
                    cur_node.sub_nodes.append(sub_node)
                # kwargs
                else:
                    cur_node.__dict__[k] = v
            return cur_node

        return _compile(data, 0, self.ROOT_NODE_NAME, None)


class Tree(object):
    def __init__(self, root: Node):
        self.root: Node = root

    def dfs(self, from_node: Node):
        # depth first
        def _loop(node: Node):
            yield node
            for each in node.sub_nodes:
                yield from _loop(each)

        return _loop(from_node)

    def bfs(self, from_node: Node):
        # init queue
        q = queue.Queue()
        q.put(from_node)

        def _clear(target_queue, output_queue):
            while not target_queue.empty():
                new_node = target_queue.get()
                yield new_node
                # and send its sub nodes to output
                for each in new_node.sub_nodes:
                    output_queue.put(each)

        while not q.empty():
            tmp = queue.Queue()
            yield from _clear(q, tmp)
            q = tmp
