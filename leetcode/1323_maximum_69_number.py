class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        i = s.find('6')
        if i >= 0:
            t=''
            t += s[0:i]
            t += '9'
            t += s[i+1:]
            return int(t)
        else:
            return int(s)