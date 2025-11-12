from typing import List
class Solution:
    def triangleNumber(self, heights: List[int]):
        heights.sort()
        count = 0
        for i in range(len(heights)-1,1,-1):
            left = 0
            right=i-1
            while left<right:
                if heights[i]<heights[left]+heights[right]:
                    count += right-left
                    right -= 1
                else:
                    left +=1
        
        return count
             