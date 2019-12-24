# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = get_length(headA), get_length(headB)
        if lenA >= lenB:
            longer = headA
            shorter = headB
            longer_len = lenA
            shorter_len = lenB
        else:
            longer = headB
            shorter = headA
            longer_len = lenB
            shorter_len = lenA
        len_diff = longer_len - shorter_len
        for _ in range(len_diff):
            longer = longer.next
        for _ in range(shorter_len):
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        return None


def get_length(node: ListNode):
    count = 0
    while node:
        node = node.next
        count += 1
    return count
