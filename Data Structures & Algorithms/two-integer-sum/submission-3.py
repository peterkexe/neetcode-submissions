class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDiff = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seenDiff:
                return [seenDiff[diff], i]
            seenDiff[num] = i