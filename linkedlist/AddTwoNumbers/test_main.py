from linkedlist.AddTwoNumbers.main import Solution, ListNode


def test_main():
    head1 = ListNode(2)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head2 = ListNode(5)
    head2.next = ListNode(6)
    head2.next.next = ListNode(4)
    solution = Solution()
    ans = solution.addTwoNumbers(head1, head2)
    assert ans.val == 7
    assert ans.next.val == 0
    assert ans.next.next.val == 8
