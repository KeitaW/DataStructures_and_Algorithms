# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        def helper(node, string=""):
            return helper(node.next, string + f"{node.val}, ") if node else string
        return helper(self)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def helper(node):
            print(node)
            if node is None:
                return
            next_node = node.next
            node.next = next_node.next
            next_node.next = node
            helper(node.next)
            return next_node
        return helper(head)
