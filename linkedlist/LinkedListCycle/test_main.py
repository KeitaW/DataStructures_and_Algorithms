from linkedlist.LinkedListCycle.main import ListNode, Solution


def test_main():
    solution = Solution()
    head = ListNode(1)
    assert solution.hasCycle(head) == False
    head.next = ListNode(2)
    head.next.next = head
    assert solution.hasCycle(head) == True
