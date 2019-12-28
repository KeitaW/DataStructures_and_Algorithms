from queue_and_stack.DesignCircularQueue.main import MyCircularQueue


def test_circular_queue():
    circularQueue = MyCircularQueue(3)
    assert circularQueue.enQueue(1) == True
    assert circularQueue.enQueue(2) == True
    assert circularQueue.enQueue(3) == True
    assert circularQueue.enQueue(4) == False
    assert circularQueue.Rear() == 3
    assert circularQueue.isFull() == True
    assert circularQueue.deQueue() == True
    assert circularQueue.enQueue(4) == True
    assert circularQueue.Rear() == 4
