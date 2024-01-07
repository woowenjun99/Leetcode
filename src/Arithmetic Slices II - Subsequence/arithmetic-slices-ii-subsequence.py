from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                difference = nums[i] - nums[j]
                dp[i][difference] += 1
                if difference in dp[j]:
                    total_count += dp[j][difference]
                    dp[i][difference] += dp[j][difference]
        return total_count

s = Solution()
ans = s.numberOfArithmeticSlices([2,4,6,8,10])
print(ans)