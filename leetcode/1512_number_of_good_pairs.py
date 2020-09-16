class Solution:
    def added_through(self,x):
        if x == 1:
            return 0
        else:
            return (x-1) + self.added_through(x-1)
    
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        
        total_pairs = 0
        for num in count.keys():
            total_pairs += self.added_through(count[num])
        return total_pairs