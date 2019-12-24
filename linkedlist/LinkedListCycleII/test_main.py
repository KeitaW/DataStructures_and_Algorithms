from linkedlist.LinkedListCycleII.main import ListNode, Solution


def test_main():
    solution = Solution()
    head = ListNode(1)
    assert solution.detectCycle(head) == None
    head.next = ListNode(2)
    head.next.next = head
    assert solution.detectCycle(head) == head
