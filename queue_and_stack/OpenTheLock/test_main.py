from queue_and_stack.OpenTheLock.main import Solution


def test_main():
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    solution = Solution()
    assert solution.openLock(deadends, target) == 6
    deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
    target = "8888"
    solution = Solution()
    assert solution.openLock(deadends, target) == -1
