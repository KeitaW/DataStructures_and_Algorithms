class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ Given a non-empty array of integers, every element appears twice except for one. Find that single one.

        
        Parameters
        ----------
        nums : List[int]
        
        Returns
        -------
        int
        """
        hash_set = set()
        for num in nums:
            if num in hash_set:
                hash_set.discard(num)
            else:
                hash_set.add(num)
        return hash_set.pop()

