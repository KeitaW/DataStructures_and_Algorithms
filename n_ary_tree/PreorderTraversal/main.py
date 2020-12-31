from typing import List


class Node:
    pass


class Node:
    def __init__(self, val: int = None, children: List[Node] = None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.result = []

    def preorder(self, root: Node) -> List[int]:
        output = []
        if root is None:
            return output
        stack = [root]
        while stack:
            node = stack.pop()
            output.append(node.val)
            for child in node.children:
                stack.append(child)
        return output

    def preorder_recur(self, root: Node) -> List[int]:
        if root is None:
            return []
        self.result.append(root.val)
        for child in root.children:
            self.preorder(child)
        return self.result

