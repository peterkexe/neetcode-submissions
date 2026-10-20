class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        pre = 1
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]
        
        suf = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suf
            suf *= nums[i]
        
        return ans
        
        # zeros = nums.count(0)
        # if zeros > 1:
        #     return [0] * len(nums)

        # total = 1
        # if zeros == 1:
        #     ans = [0] * len(nums)
        #     for i, num in enumerate(nums):
        #         if num == 0:
        #             ans[i] = 1
        #         else:
        #             total *= num
        #     return [a * total for a in ans]
        
        # if zeros == 0:
        #     ans = [1] * len(nums)
        #     for i, num in enumerate(nums):
        #         ans[i] = num
        #         total *= num
        #     return [total // a for a in ans]