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
        print(f"init l1: {l1}")
        print(f"init l2: {l2}")
        if l1 is None:
            print("l1 is None")
            print(f"l1: {l1}")
            print(f"l2: {l2}")
            return l2
        if l2 is None:
            print("l2 is None")
            print(f"l1: {l1}")
            print(f"l2: {l2}")
            return l1
        if l1.val < l2.val:
            print("l1 < l2")
            print(f"l1: {l1}")
            print(f"l2: {l2}")
            l1.next = self.mergeTwoLists(l1.next, l2)
            print("l1 < l2 after")
            print(f"l1: {l1}")
            print(f"l2: {l2}")
            return l1
        else:
            print("l1 > l2")
            print(f"l1: {l1}")
            print(f"l2: {l2}")
            l2.next = self.mergeTwoLists(l1, l2.next)
            print("l1 > l2 after")
            print(f"l1: {l1}")
            print(f"l2: {l2}")
            return l2
