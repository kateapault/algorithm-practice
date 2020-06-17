class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        
        for i in range(0,2*n):
            if i % 2 == 0:
                nums[i] = x[i//2]
            else:
                nums[i] = y[i//2]
        return nums