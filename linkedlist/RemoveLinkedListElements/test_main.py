from linkedlist.RemoveLinkedListElements.main import ListNode, Solution


def test_main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    ans = solution.removeElements(head, 3)
    assert ans.val == 1
    assert ans.next.val == 2
    assert ans.next.next.val == 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(4)
    solution = Solution()
    ans = solution.removeElements(head, 2)
    assert ans.val == 1
    assert ans.next.val == 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    ans = solution.removeElements(head, 1)
    assert ans.val == 2
    assert ans.next.val == 3
    assert ans.next.next.val == 4
    head = ListNode(1)
    head.next = ListNode(1)
    solution = Solution()
    ans = solution.removeElements(head, 1)
    assert ans is None
