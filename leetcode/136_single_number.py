class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        f = {}
        for x in nums:
            if x in f:
                del f[x]
            else:
                f[x] = 1
        return list(f.keys())[0]