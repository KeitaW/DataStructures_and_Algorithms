# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        node = self
        string = ""
        while node is not None:
            string += f"{node.val}, "
            node = node.next
        return string


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
