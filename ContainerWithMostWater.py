from typing import List


class Solution:
    def max_area(self, heights: List[int]):
        size = len(heights)
        left, right, base, area = 0, size-1, size-1, 0

        if base >0  and left < right :
            area = base*min(heights[left] , heights[right])
            base -= 1
        
        while base > 0 and left < right :
            a_l = base * min(heights[left+1],heights[right])
            a_r = base * min(heights[left],heights[right-1])
            if a_l < a_r :
                right -= 1

                if area < a_r:
                    area = a_r

            else:
                left += 1

                if area < a_l:
                    area = a_l

            base -= 1
        
        return area
                