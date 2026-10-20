class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)
        # ans    = [1] * len(nums)

        # for i in range(len(nums)):
        #     pre = nums[:i]
        #     for p in pre:
        #         prefix[i] *= p
            
        #     suf = nums[i+1:]
        #     for s in suf:
        #         suffix[i] *= s
        
        # for i in range(len(nums)):
        #     ans[i] = prefix[i] * suffix[i]
        # return ans
        
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)

        total = 1
        if zeros == 1:
            ans = [0] * len(nums)
            for i, num in enumerate(nums):
                if num == 0:
                    ans[i] = 1
                else:
                    total *= num
            return [a * total for a in ans]
        
        if zeros == 0:
            ans = [1] * len(nums)
            for i, num in enumerate(nums):
                ans[i] = num
                total *= num
            return [total // a for a in ans]