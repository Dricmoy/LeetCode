#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums_as_set = set(nums)
        
        for index, val in enumerate(nums):
            if (val != 0) and (val - 1) not in nums_as_set: #since given values are in the range 0, n, if it was 1, n modify differently
                return (val - 1)
            
        return len(nums)
        
# @lc code=end