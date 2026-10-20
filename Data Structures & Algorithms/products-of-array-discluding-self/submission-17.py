class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
                ans[i] = 1 / num
                total *= num
            return [int(a * total) for a in ans]