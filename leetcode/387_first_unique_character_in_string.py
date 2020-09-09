class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) < 1:
            return -1
        elif len(s) == 1:
            return 0
        l = {}
        for x in s:
            if x in l:
                l[x] += 1
            else:
                l[x] = 1
        
        t = len(s)
        for k in list(l.keys()):
            if l[k] == 1:
                if s.index(k) < t:
                    t = s.index(k)
        
        if t == len(s):
            return -1
        else:
            return t