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
        if head is None or head.next is None:
            return head
        # Current Head and Previous Head
        curr, prev = head.next, head
        while curr is not None:
            next = curr.next
            if next is None:
                # End of List
                self.head = curr
            curr.next = prev
            curr, prev = next, curr
        return self.head
