from math import log

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1:
            return False
        else:
            return int(log(num,4)) == log(num,4)