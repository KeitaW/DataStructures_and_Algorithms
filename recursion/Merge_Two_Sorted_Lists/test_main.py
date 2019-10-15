from recursion.Merge_Two_Sorted_Lists.main import Solution, ListNode


def test_main():
    node1 = ListNode(1)
    node1.next = ListNode(2)
    node1.next.next = ListNode(4)
    print(f"List1: {node1}")
    node2 = ListNode(1)
    node2.next = ListNode(3)
    node2.next = ListNode(4)
    print(f"List2: {node2}")
    expected = ListNode(1)
    expected.next = ListNode(1)
    expected.next.next = ListNode(2)
    expected.next.next = ListNode(2)
    expected.next.next.next = ListNode(3)
    expected.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next = ListNode(4)
    solution = Solution()
    print("Result: ", solution.mergeTwoLists(node1, node2))
    print("Expected: ", expected)
