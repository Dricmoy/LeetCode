#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        
        left = 1 #base case
        
        for i in range(n):
            arr[i] *= left
            left *= nums[i]
        

        right = 1
        
        for i in range(n-1, -1, -1):
            arr[i] *= right
            right *= nums[i]
            
        return arr
        
# @lc code=end