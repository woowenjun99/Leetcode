class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n
        a = 1
        b = 2
        c = 3
        """
        Notice that dp[i] = dp[i - 1] + dp[i - 2]. Therefore, we need a variable
        that stores these 3 variables
        """
        for i in range(3, n):
            a, b = b, c
            c = a + b
        return c