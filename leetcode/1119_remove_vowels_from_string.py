class Solution:
    def removeVowels(self, S: str) -> str:
        n = ''
        for x in S:
            if x not in 'aeiou':
                n += x
        return n