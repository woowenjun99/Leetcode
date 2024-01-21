"""
Topic: Dynamic Problem

Notice that the subproblem can be broken down into the following:

dp[i] = max(num + dp[i - 2], dp[i - 1])
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        left = right = 0
        for num in nums:
            temp = num + left
            left = right
            right = max(left, temp)
        return max(left, right)