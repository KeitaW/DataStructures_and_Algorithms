class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ Given two arrays, write a function to compute their intersection.
        Example 1:

        Input: nums1 = [1,2,2,1], nums2 = [2,2]
        Output: [2]
        
        Parameters
        ----------
        nums1 : List[int]
        nums2 : List[int]
        
        Returns
        -------
        List[int]
        """
        set1, set2 = set(nums1), set(nums2)
        return set1.intersection(set2)

