class Solution:
    def rob(self, nums: List[int]) -> int:
        # f[i] so tien lay duoc lon nhat tai nha thu i
        # tai nha thu i
            # 1. Khong lay -> f[i] = f[i-1]
            # 2. Lay -> f[i] = f[i-2] + nums[i]
        # f[i] = max(f[i-1], f[i-2] + nums[i])
        # n = len(nums)
        # if n == 1: return nums[0]

        # f = [0] * n
        # f[0] = nums[0]
        # f[1] = max(f[0], nums[1])

        # for i in range(2, n):
        #     f[i] = max(f[i-1], f[i-2] + nums[i])

        # return f[-1]

        # f1, f2 <=> f[i-1], f[i-2]
        f1 = f2 = 0
        for house in nums:
            f1, f2 = max(f1, f2 + house), f1
        
        return f1

