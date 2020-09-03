class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ss = ''
        l = len(s)
        if len(s) < 2:
            return False
        elif len(set(s)) == 1:
            return True
        else:
            for i in range(0,len(s)//2):
                ls = len(ss)
                if ls < 2:
                    ss += s[i]
                else:
                    if l % ls == 0:
                        if ss * (l//ls) == s:
                            return True
                        else:
                            ss += s[i]
                    else:
                        ss += s[i]
            return ss * 2 == s