#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:        
        total_time = 0
        
        for count, val in enumerate(points):
            if count == len(points) - 1: #we hit the last value, don't try anything
                return total_time
            
            # get the next point
            next = points[count + 1]
            x = abs(val[0] - next[0])
            y = abs(val[1] - next[1])
            
            if x > y:
                total_time += x
            else:
                total_time += y
        
        
# @lc code=end