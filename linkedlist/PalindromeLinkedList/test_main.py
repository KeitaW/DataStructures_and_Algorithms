from linkedlist.PalindromeLinkedList.main import ListNode, Solution, find_middle, compare_list, reverse_list


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


def test_reverse_list():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    reverse_list(head)
    assert head.val == 3
    assert head.next.val == 2
    assert head.next.nextval == 1


def test_compare_list():
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert compare_list(head1, head2)
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head2 = ListNode(1)
    head2.next = ListNode(3)
    assert not compare_list(head1, head2)


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
