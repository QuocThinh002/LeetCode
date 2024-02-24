class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Time complexity: O(n)
# Space complexity: O(n)

# Dynamic Programming Solution for Climbing Stairs Problem
# Definition, dp[i]: The number of distinct ways to reach the ith stair.

# Explanation:
# To reach the ith stair, you can either come from the i - 1th or i - 2th stair.
# The number of ways to reach the i - 1th stair is dp[i - 1].
# The number of ways to reach the i - 2th stair is dp[i - 2].
# The total number of ways to reach the ith stair is dp[i - 1] + dp[i - 2].

# Formula: dp[i] = dp[i - 1] + dp[i - 2] if i > 1.
# dp[0] = 1 (there is 1 way to reach the 0th stair, which is to not move).
# dp[1] = 1 (there is 1 way to reach the 1st stair, which is to move 1 step from the 0th stair).