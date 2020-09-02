class Solution:
    def diff(self,num1,num2):
        if num2 < 0:
            return num1 - num2
        elif num1 < 0:
            return num2 - num1
        else:
            return abs(num1 - num2)
    
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0:
            if len(set(nums)) == len(nums):
                return False
        for i in range(0,len(nums)-1):
            p1 = i
            if k > 1:
                for x in range(1,k+1):
                    if p1 + x < len(nums):
                        p2 = p1 + x
                        print(self.diff(nums[p1],nums[p2]))
                        if self.diff(nums[p1],nums[p2]) <= t:
                            return True
            elif k == 1:
                p2 = p1 + 1
                print(self.diff(nums[p1],nums[p2]))
                if self.diff(nums[p1],nums[p2]) <= t:
                    return True
            else:
                return False
        return False