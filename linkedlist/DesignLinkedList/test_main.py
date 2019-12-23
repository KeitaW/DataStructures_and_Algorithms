from linkedlist.DesignLinkedList.main import MyLinkedList


def test_my_linked_list():
    linked_list = MyLinkedList()
    print(linked_list)
    linked_list.addAtHead(1)
    print(linked_list)
    linked_list.addAtTail(3)
    print(linked_list)
    linked_list.addAtIndex(1, 2)
    print(linked_list)
    assert linked_list.get(1) == 2
    print(linked_list)
    linked_list.deleteAtIndex(1)
    print(linked_list)
