from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for idx in range(len(nums) - k):
            for l in range(k - 1):
                if nums[idx] == nums[idx + l]:
                    return True
        else:
            return False

