from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """[summary]
        Assumption: "numbers" is sorted

        Parameters
        ----------
        numbers : List[int]
        target : int

        Returns
        -------
        List[int]
             Two indices that 
        """
        small, large = 0, len(numbers) - 1
        while True:
            summed = numbers[small] + numbers[large]
            if summed == target:
                return small+1, large+1
            if summed > target:
                large -= 1
            else:
                small += 1

    def naive_twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return sorted([i+1, j+1])
