from linkedlist.RemoveNthNodeFromEndOfList.main import ListNode, Solution


def test_main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    solution.removeNthFromEnd(head, 2)
    assert head.val == 1
    assert head.next.val == 2
    assert head.next.next.val == 4
    head = ListNode(1)
    head.next = ListNode(2)
    solution.removeNthFromEnd(head, 2)
    assert head.val == 2
