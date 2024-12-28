#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_check = {}
        
        for count, val in enumerate(nums):
            if target - val not in to_check:
                to_check[val] = count
            else:
                break
        return [count, to_check[target-val]]   
     
            
# @lc code=end

