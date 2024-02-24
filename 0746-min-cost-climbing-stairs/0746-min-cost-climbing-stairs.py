class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f[i] la chi phi nho nhat de leo len duoc bac thang thu i
        # de leo len duoc bac thang thu i, chung ta co the buoc tu bac thang i-1 or i-2
        # i-1 -> i
        # f[i] = f[i-1] + cost[i-1]
        # i-2 -> i
        # f[i] = f[i-2] + cost[i-2]
        # f[i] = min(f[i-1] + cost[i-1], f[i-2] + cost[i-2])
        
        n = len(cost)
        f = [0] * (n+1)
        for i in range(2, n+1):
            f[i] = min(f[i-1] + cost[i-1], f[i-2] + cost[i-2])

        return f[n]