#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        first, second = 1, 2
        
        for i in range(3, n + 1): #since range isn't inclusive
            cur = first + second
            first = second #this is preparation for next iter
            second = cur
            
        return second
        
# @lc code=end

