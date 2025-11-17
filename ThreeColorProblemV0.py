from typing import List
class Solution:
    def sortColors(self, nums: List[int]):
        colorCounts = [0,0,0]
        for i in range(len(nums)):
            if nums[i]==0:
                colorCounts[0] += 1
            elif nums[i]==1:
                colorCounts[1] += 1
            else: 
                colorCounts[2] += 1
        
        next_position = 0
        for i in range(len(colorCounts)):
            j, k= next_position, i
            while colorCounts[i] != 0:
                if nums[j] != i:
                    j +=1
                    continue
                else:
                    nums[next_position], nums[j] = nums[j], nums[next_position]
                    next_position +=1
                    colorCounts[i] -=1
                    j +=1
        return nums


        
 