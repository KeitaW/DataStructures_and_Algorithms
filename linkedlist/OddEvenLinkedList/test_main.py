from linkedlist.OddEvenLinkedList.main import ListNode, Solution


def test_main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    solution.oddEvenList(head)
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 2
    assert head.next.next.next.val == 4

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution = Solution()
    solution.oddEvenList(head)
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 5
    assert head.next.next.next.val == 2
    assert head.next.next.next.next.val == 4

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = ListNode(7)
    head.next.next.next.next.next.next.next = ListNode(8)
    solution = Solution()
    solution.oddEvenList(head)
    assert head.val == 1
    assert head.next.val == 3
    assert head.next.next.val == 5
    assert head.next.next.next.val == 7
    assert head.next.next.next.next.val == 2
    assert head.next.next.next.next.next.val == 4
    assert head.next.next.next.next.next.next.val == 6
    assert head.next.next.next.next.next.next.next.val == 8
