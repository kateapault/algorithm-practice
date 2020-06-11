class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        while j < k:
            nums.insert(0,nums.pop())
            j += 1