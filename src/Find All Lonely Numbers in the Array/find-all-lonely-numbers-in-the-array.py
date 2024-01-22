from typing import List
from collections import Counter

class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for key in counter:
            if counter[key] == 1 and key - 1 not in counter and key + 1 not in counter:
                result.append(key)
        return result