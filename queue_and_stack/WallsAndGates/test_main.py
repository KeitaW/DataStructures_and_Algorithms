from queue_and_stack.WallsAndGates.main import Solution

INF = 2 ** 31 - 1


def test_main():
    solution = Solution()
    rooms = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]
    solution.wallsAndGates(rooms)
    assert rooms == [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]
