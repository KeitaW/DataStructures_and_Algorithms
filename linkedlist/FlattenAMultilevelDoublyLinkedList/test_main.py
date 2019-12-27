from linkedlist.FlattenAMultilevelDoublyLinkedList.main import Solution, Node


def range_linked_list(start=0, end=4):
    head = node = Node(-1)
    prev = None
    for i in range(start, end):
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
    head = range_linked_list(start=3, end=5)
    assert head.val == 3
    assert head.next.val == 4


def test_main():
    head1 = range_linked_list(1, 7)
    head2 = range_linked_list(7, 11)
    head3 = range_linked_list(11, 13)
    head1.next.next.child = head2
    head2.next.child = head3
