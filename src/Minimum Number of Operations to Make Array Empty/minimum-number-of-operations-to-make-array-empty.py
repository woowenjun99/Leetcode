from typing import List
from collections import Counter
from math import ceil

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        occurences = dict(Counter(nums))
        optimal = 0
        for value in occurences.values():
            if value == 1: return -1
            optimal += ceil(value / 3)
        return optimal