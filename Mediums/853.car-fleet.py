#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for (p, s) in zip(position, speed)]
        
        pair.sort(reverse=True)
        
        fleets = []
        
        for p, s in pair:
            fleets.append((target - p)/s)
            
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]: # the time needed by the fleet that just came is less than the one before it meaning it will become the same fleet
                fleets.pop()
        
        return len(fleets)
        
        
# @lc code=end