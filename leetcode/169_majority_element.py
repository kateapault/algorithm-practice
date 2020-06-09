class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        elemnt_count = {}
        n = len(nums) / 2
        for e in nums:
            if element in element_count:
                element_count[element] += 1
            else:
                element_count[element] = 1
            
            if element_count[element] > n:
                return element