from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        response = []
        for num in nums:
            if not response or num > response[-1]:
                response.append(num)
            else:
                index = bisect_left(response, num)
                response[index] = num
        return len(response)