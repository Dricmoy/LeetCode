#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort() #O(nlog(n))

        for count, val in enumerate(nums):
            if count > 0 and val == nums[count - 1]: #gets rid of duplicate a vals
                continue
            
            l, r = count + 1, len(nums) - 1
            
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res
        
# @lc code=end