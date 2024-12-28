#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # easy bruteforcewould be to do it on each
        
        # maybe sorting is the best way
        temp = sorted(nums)
        
        counts = {}
        
        for index, val in enumerate(temp):
            if val not in counts:
                counts[val] = index # the index will already be the count of things that are smaller due to it being sorted
                    
        for index, val in enumerate(nums):
            nums[index] = counts[val]
        
        return nums
# @lc code=end