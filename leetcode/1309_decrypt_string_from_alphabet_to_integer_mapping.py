class Solution:
    def freqAlphabets(self, s: str) -> str:
        ab = 'abcdefghijklmnopqrstuvwxyz'
        a = {}
        for i in range(1,27):
            if i > 9:
                a[f"{i}#"] = ab[i-1]
            else:
                a[f"{i}"] = ab[i-1]
        #######
        p = []
        i = 0
        while i < len(s):
            if i + 2 < len(s):
                if s[i+2] == '#':
                    p.append(s[i:i+3])
                    i += 3
                else:
                    p.append(s[i])
                    i += 1
            else:
                p.append(s[i])
                i += 1
        
        o = ''
        for x in p:
            o += a[x]
        return o
