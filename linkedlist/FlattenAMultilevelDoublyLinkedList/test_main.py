from linkedlist.FlattenAMultilevelDoublyLinkedList.main import Solution, Node


def range_linked_list(start=0, end=4):
    head = node = Node(-1)
    prev = None
    for i in range(0, 4):
        node.next = Node(i)
        node.prev = prev
        prev = node
        node = node.next
    return head.next


def test_range_linked_list():
    head = range_linked_list(start=0, end=4)
    assert head.val == 0
    assert head.next.val == 1
    assert head.next.next.val == 2
    assert head.next.next.next.val == 3
