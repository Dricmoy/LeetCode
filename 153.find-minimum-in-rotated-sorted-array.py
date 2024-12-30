#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(log n) means related to sorting somehow
        
        # since it needs to be 0(log n) can I not just sort :sob I cannot since that is a nlogn solution in python which uses Timsort
        
        # always think binary search for logn time complexity requirement
        # even more obvious due to it being on a sorted array
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1                
        return nums[left]
        
# @lc code=end