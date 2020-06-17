def binary_search(target, nums):
    
    floor_index = -1    # number to the left of ind 0 NOT last index
    ceiling_index = len(nums)
    
    while floor_index + 1 < ceiling_index:
        
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance
        
        guess_value = nums[guess_index]
        
        if guess_value == target:
            return True
        elif guess_value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index
            
    return False

n = [1,2,4,5,6,7]

print(binary_search(2,n)) # should return True
print(binary_search(3,n)) # should return False