# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.
        Example:
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        Explanation: 342 + 465 = 807.

        Parameters
        ----------
        l1 : ListNode
        l2 : ListNode

        Returns
        -------
        ListNode
        """
        head = node = ListNode(-1)  # Head is dummy
        carry = 0
        while (l1 is not None) or (l2 is not None):
            num1 = l1.val if l1 is not None else 0
            num2 = l2.val if l2 is not None else 0
            total = num1 + num2 + carry
            node.next = ListNode(total % 10)
            carry = total // 10
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            node = node.next
        if carry > 0:
            node.next = ListNode(carry)
        return head.next
