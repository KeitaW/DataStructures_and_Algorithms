# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")


def find_middle(head: ListNode):
    slow = fast = head
    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ Given a singly linked list, determine if it is a palindrome.
        Input: 1->2->2->1
        Output: true

        Parameters
        ----------
        head : ListNode

        Returns
        -------
        bool
        """
        tail = head
        while tail.next is not None:
            tail = tail.next
