#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False 
            
        countS = {}
        countT = {}
        
        for c in s:
            countS[c] = 1 + countS.get(c, 0)
            
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        for c in countS:
            if countS[c] != countT.get(c , 0):
                return False
        return True
        
# @lc code=end

