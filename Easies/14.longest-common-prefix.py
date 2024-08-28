#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: # type: ignore
        if not strs: #easiest way  to check for empty
            return ''
        
        prefix = strs[0]
        
        for str in strs[1:]:
            while not str.startswith(prefix):
                prefix = prefix[:-1] #this removes the last character with slicing, same as [0:-1]
                
                if not prefix: #if prefix is empty by the last scan, this means none exists
                    return ''
                
        return prefix
                        
            
# @lc code=end

