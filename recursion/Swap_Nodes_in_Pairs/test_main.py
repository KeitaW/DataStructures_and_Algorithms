from recursion.Swap_Nodes_in_Pairs.main import Solution, ListNode


def test_swapPairs():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    expected = ListNode(2)
    expected.next = ListNode(1)
    expected.next.next = ListNode(4)
    expected.next.next.next = ListNode(3)

    solution = Solution()
    solution.swapPairs(head)
    while expected:
        print("hey", head.val, expected.val)
        assert head.val == expected.val
        head = head.next
        expected = expected.next
