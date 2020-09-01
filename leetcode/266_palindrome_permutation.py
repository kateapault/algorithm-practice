class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        o = []
        for x in s:
            if x in o:
                o.remove(x)
            else:
                o.append(x)
        return len(o) < 2