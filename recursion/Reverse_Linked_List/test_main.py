from recursion.Reverse_Linked_List.main import Solution, ListNode


def test_main():
    p_node = ListNode(1)
    head = p_node
    for i in range(2, 6):
        node = ListNode(i)
        p_node.next = node
        p_node = node
    node = head
    while node:
