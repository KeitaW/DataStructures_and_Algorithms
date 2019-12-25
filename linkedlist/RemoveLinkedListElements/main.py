# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")


class Solution:
    def __init__(self):
        self.head = None

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        self.head = head
        while (self.head is not None) and (self.head.val == val):
            self.head = self.head.next
        if (self.head is None) or (self.head.next is None):
            return self.head
        prev, curr = self.head, self.head.next
        while curr is not None:
            if curr.val == val:
                prev.next = prev.next.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return self.head
