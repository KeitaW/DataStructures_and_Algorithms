class Node:
    def __init__(self, val, prev: 'Node' = None, next: 'Node' = None, child: 'Node' = None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self, string=""):
        return string + f"{self.val}, " + (self.next.__str__() if self.next else "")


class Solution:
    def flatten(self, head: Node) -> Node:
        """You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.
        Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

        Example 1:
        Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
        Output: [1,2,3,7,8,11,12,9,10,4,5,6]

        Parameters
        ----------
        head : Node
            [description]

        Returns
        -------
        Node
            [description]
        """
        if head is None:
            return head
        # Pseudo head
        flatten = Node(-1, None, head, None)
        curr, prev = head, flatten
        stack = [head]
        while stack:
            curr = stack.pop(-1)
            prev.next = curr
            curr.prev = prev
            if curr.next is not None:
                stack.append(curr.next)
            if curr.child is not None:
                stack.append(curr.child)
                curr.child = None
            prev = curr
        flatten.next.prev = None
        return flatten.next
