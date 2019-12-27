from linkedlist.PalindromeLinkedList.main import ListNode, Solution, find_middle


def test_find_middle():
    head = ListNode(1)
    assert find_middle(head).val == 1
    head = ListNode(1)
    head.next = ListNode(2)
    assert find_middle(head).val == 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    assert find_middle(head).val == 2
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    assert find_middle(head).val == 3


def test_main():
    return
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    solution = Solution()
    assert solution.isPalindrome(head) == True
    head = ListNode(1)
    head.next = ListNode(2)
    solution = Solution()
    assert solution.isPalindrome(head) == False
