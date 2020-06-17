class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        r = [nums[0]]
        i = 1
        while i < len(nums):
            r.append(r[i-1]+nums[i])
            i += 1
        return r