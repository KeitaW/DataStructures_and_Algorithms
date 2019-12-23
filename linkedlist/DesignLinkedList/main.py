
class Node:
    def __init__(self, val=-1):
        self.val: int = val
        self.next_node: Node = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def __str__(self):
        if not self.head:
            return ""

        def recur(index, string):
            if self.size == index:
                return string
            else:
                recur(index+1, string + str(self.get(index+1)))

        return recur(0, str(self.get(0)))

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        node = self.head
        for _ in range(index - 1):
            node = node.next_node
        return node.val

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        node = self.head
        new_node = Node(val)
        if index == 0:
            new_node.next = node
            self.head = new_node
        else:
            for _ in range(index - 1):
                node = node.next_node
            new_node.next = node.next_node
            node.next_node = new_node
        self.size += 1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return

        node = self.head
        if index == 0:
            self.head = self.head.next_node
        else:
            for _ in range(index - 1):
                node = node.next_node
            node.next_node = node.next_node.next_node
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
