from pytest import fixture

from tree.binary_tree.Heap.main import Heap


# @fixture
def heap_instance():
    return Heap(heap=[19, 12, 15, 10, 7, 6, 1, 3, 7, 5, 3, 2])


if __name__ == "__main__":
    print(heap_instance())
