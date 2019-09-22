"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        node = root
        current = [node]
        while current:
            next_level = []
            prev_node = None
            for node in current:
                if prev_node:
                    prev_node.next = node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                prev_node = node
            current = next_level
        return root
