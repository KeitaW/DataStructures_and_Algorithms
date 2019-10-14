class ListNode:
    # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")


class Solution:
    def __init__(self):
        self.head = None

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        def flip(curr: ListNode, prev: ListNode):
            if curr.next is None:
                self.head = curr
                curr.next = prev
                return
            next = curr.next
            curr.next = prev
            flip(next, curr)
        flip(head, None)
        return self.head
