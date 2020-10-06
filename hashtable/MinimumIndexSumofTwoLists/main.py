from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_interests = set(list1).intersection(set(list2))
        list_index_sums = []
        choices = []
        while common_interests:
            item = common_interests.pop()
            list_index_sums.append(list1.index(item) + list2.index(item))
            choices.append(item)
        least_index_sum = min(list_index_sums)
        return [
            choice
            for index_sum, choice in sorted(zip(list_index_sums, choices))
            if index_sum == least_index_sum
        ]

