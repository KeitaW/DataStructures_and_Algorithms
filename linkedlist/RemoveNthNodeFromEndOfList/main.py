# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        from_head = from_nth = head
        if head.next == None:
            return None
        for _ in range(n):
            from_nth = from_nth.next
        if from_nth == None:
            # n is length of the list
            head = head.next
        else:
            while from_nth.next:
                from_nth = from_nth.next
                from_head = from_head.next
            from_head.next = from_head.next.next
        return head
