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

    def oddEvenList(self, head: ListNode) -> ListNode:
        """" Given a singly linked list, group all odd nodes together followed by the even nodes.
        Please note here we are talking about the node number and not the value in the nodes.
        You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

        Example:
        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL
        Parameters
        ----------
        head : ListNode

        Returns
        -------
        ListNode
        """
        if (head is None) or (head.next is None):
            return head
        odd, even = head, head.next
        first_even = head.next
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        odd.next = first_even
        return head
