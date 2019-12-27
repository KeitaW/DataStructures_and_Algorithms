# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")


def find_middle(head: ListNode):
    slow = fast = head
    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow


def compare_list(head1: ListNode, head2: ListNode):
    while (head1 is not None) and (head2 is not None):
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True


def reverse_list(head: ListNode):
    pre, peri, post = None, head, head.next
    while peri is not None:
        post = peri.next
        peri.next = pre
        pre = peri
        peri = post
    head = pre


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
