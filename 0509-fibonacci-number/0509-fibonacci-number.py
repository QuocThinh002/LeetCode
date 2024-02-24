class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        f = [0, 1] + [0] * (n-1)

        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
            
        return f[n]