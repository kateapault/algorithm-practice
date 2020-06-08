class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        current_substring = ''
        
        for i in range(0,len(s)):
            if s[i] in current_substring:
                ind = current_substring.find(s[i])
                current_substring = current_substring[ind+1:] + s[i]
            else:
                current_substring += s[i]
        
            if len(current_substring) > longest_substring_length:
                longest_substring_length = len(current_substring)

        return longest_substring_length