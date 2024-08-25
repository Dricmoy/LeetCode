#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #I would need to check if the first of each element
        #has a corresponding last element until I reach the half of
        #the string?

        x = str(x)
        
        reverse = x[::-1]
            
        if x == reverse:
            return True
        else:
            return False
        


    
# @lc code=end