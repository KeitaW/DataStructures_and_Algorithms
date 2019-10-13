import cProfile
import pstats
from line_profiler import LineProfiler
import pytest

from misc.LRU_Cache.main import LRUCache


def test_LRUCache():
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)  # evicts key 2
    assert cache.get(2) == -1  # -1: not found
    cache.put(4, 4)  # evicts key 1
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


@pytest.mark.parametrize("capacity, methods, inputs, expected_values", (
    (
        2,
        ("put", "put", "get", "put", "get", "put", "get", "get", "get"),
        ((1, 1), (2, 2), 1, (3, 3), 2, (4, 4), 1, 3, 4),
        (None, None, 1, None, -1, None, -1, 3, 4)
    ),
    (
        2,
        ("get", "put", "get", "put", "put", "get", "get"),
        ((2), (2, 6), (1), (1, 5), (1, 2), (1), (2)),
        (-1, None, -1, None, None, 2, 6)
    )
))
def test_LRUCache_parametrize(capacity, methods, inputs, expected_values):
    cache = LRUCache(capacity=capacity)
    for idx, (method, input, expected_value) in enumerate(zip(methods, inputs, expected_values)):
        print(f"Test case: {idx}")
        print(method, input, expected_value)
        if method == "put":
            assert cache.put(*input) == expected_value
        elif method == "get":
            assert cache.get(input) == expected_value
        print(f"Current cach: {cache.cache}")
        print(f"Current cach: {cache.lru}")


def profile_LRUCache():
    CACHE_SIZE = 2**20
    cache = LRUCache(capacity=CACHE_SIZE)
    for _ in range(CACHE_SIZE):
        cache.put(_, _)
        cache.get(1)
    cache.get(CACHE_SIZE + 1)


if __name__ == "__main__":
    print("Line profile")
    profiler = LineProfiler()
    profiler.add_function(LRUCache.get)
    profiler.add_function(LRUCache.put)
    profiler.runcall(profile_LRUCache)
    profiler.print_stats()
    print("cProfile")
    profiler = cProfile.Profile(subcalls=True)
    profiler.enable()
    profile_LRUCache()
    profiler.disable()
    profiler.print_stats()
