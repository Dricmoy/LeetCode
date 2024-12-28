#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # the integers are not distinct
        # we need to return an array of integers that do not appear in nums
        # they need to be in the range of 1 to n, iteration begins from 0
        
        # easiest way is to use a set to eliminate dups
        
        nums_as_set = set(nums)
        
        res = [] #the array to store the resulting disappeared list
        
        # otherwise we definitely are missing something
        for i in range(len(nums)): #so from 0, n - 1
            i = i + 1 # so this makes it start from 0 and ends in n
            if i not in nums_as_set:
                res.append(i)
        return res
# @lc code=end