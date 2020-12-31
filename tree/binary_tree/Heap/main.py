from typing import List


class Heap:
    def __init__(self, heap: List[int]):
        self.heap = heap

    def left_idx(self, idx: int):
        child_idx = 2 * idx + 1
        return child_idx if child_idx < len(self.heap) - 1 else None

    def right_idx(self, idx: int):
        child_idx = 2 * idx + 2
        return child_idx if child_idx < len(self.heap) - 1 else None

    def parent_idx(self, idx: int):
        parent_idx = (idx - 1) // 2
        return parent_idx if parent_idx < len(self.heap) - 1 else None

    def __str__(self, idx=0, level=0, right=False):
        return (
            "    " * (level - 1)
            + (" └──" if right else (" ├──" if level != 0 else ""))
            + " "
            + str(self.heap[idx])
            + "\n"
            + (self.__str__(self.left_idx(idx), level + 1, False)
               if self.left_idx(idx) else "")
            + (self.__str__(self.right_idx(idx), level + 1, True)
               if self.right_idx(idx) else "")
        )
