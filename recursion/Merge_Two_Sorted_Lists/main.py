# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")

    # def __eq__(self, other):
    #    def eq_node(node1, node2):
    #        return node1.val == node2.val
    #    node1 = self
    #    node2 = other
    #    while node1 is not None:
    #        print(node1, node2)
    #        if not eq_node(node1, node2):
    #            return False
    #    return True


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        pre_node = ListNode(-1)
        node = pre_node
        while True:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
            if l1 is None or l2 is None:
                break
        while l1 is not None:
            node.next = l1
            l1 = l1.next
            node = node.next

        while l2 is not None:
            node.next = l2
            l2 = l2.next
            node = node.next

        return pre_node.next

    def mergeTwoLists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
