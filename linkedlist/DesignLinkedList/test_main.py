from linkedlist.DesignLinkedList.main import MyLinkedList


def test_my_linked_list():
    linked_list = MyLinkedList()
    print("1", linked_list)
    linked_list.addAtHead(1)
    print("2", linked_list)
    linked_list.addAtTail(3)
    print("valcheck", linked_list.head.next_node.val)
    print("3", linked_list)
    linked_list.addAtIndex(1, 2)
    print("4", linked_list)
    assert linked_list.get(1) == 2
    print("5", linked_list)
    linked_list.deleteAtIndex(1)
    print("6", linked_list)
