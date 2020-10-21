from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        for idx in range(len(nums)):
            if nums[idx] in window:
                return True
            window.add(nums[idx])
            if len(window) > k:
                window.remove(nums[idx - k])
        return False

    def containsNearbyDuplicate_naive(self, nums: List[int], k: int) -> bool:
        for idx in range(len(nums)):
            for l in range(max(idx - k, 0), idx):
                if nums[idx] == nums[l]:
                    return True
        else:
            return False
