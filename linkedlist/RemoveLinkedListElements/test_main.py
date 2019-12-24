from linkedlist.RemoveLinkedListElements.main import ListNode, Solution


def test_main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    solution.removeElements(head, 3)
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)
    solution = Solution()
    solution.removeElements(head, 2)
    assert head.val == 1
    assert head.next.val == 4
