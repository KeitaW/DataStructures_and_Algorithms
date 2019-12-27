from linkedlist.PalindromeLinkedList.main import ListNode, Solution


def test_main():
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
