from linkedlist.IntersectionOfTwoLinkedList.main import ListNode, get_length, Solution


def test_get_length():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert get_length(head) == 3


def test_main():
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head2 = ListNode(5)
    head2.next = head1.next.next
    intersection = head1.next.next
    solution = Solution()
    assert solution.getIntersectionNode(head1, head2) == intersection
