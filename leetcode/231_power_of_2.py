class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        e = 0
        while 2**e < n:
            e += 1
        return 2**e == n