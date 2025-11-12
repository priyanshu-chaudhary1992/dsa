from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]):
        next_non_zero_position = 0
        
        for i in range(len(nums)):
            
            if nums[i] != 0:
                
                nums[next_non_zero_position],nums[i] = nums[i],nums[next_non_zero_position]
                next_non_zero_position +=1
            
        return nums
