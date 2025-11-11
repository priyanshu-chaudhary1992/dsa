from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        left, right = 0, (len(nums)-1)
        while left<right:
            if nums[left]+nums[right]==target:
                return True

            if target>nums[left]+nums[right]:
                left += 1
            else:
                right -=1
        return False