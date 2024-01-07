from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appeared = {}
        for index, num in enumerate(nums):
            if num in appeared:
                return [index, appeared[num]]
            appeared[target - num] = index