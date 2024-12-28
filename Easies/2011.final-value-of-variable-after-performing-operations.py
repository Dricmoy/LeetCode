#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for operation in operations:
            if "+" in operation:
                res += 1
            else:
                res-= 1
        
        return res
        
# @lc code=end

