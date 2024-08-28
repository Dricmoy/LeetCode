#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')':'(' , '}':'{', ']':'['} #key value hashmap
        
        stack = [] #stack to keep track of opening brackets
        
        for char in s:
            if char in matching:
                if stack and stack[-1] == matching[char]: #ensures if the opening bracket in stack corresponds to the correct matching_pair
                    stack.pop() #this will pop the opening bracket
                else:
                    return False
            else:
                stack.append(char) #stack will always append opening brackets when it works
        
        return not stack
        
# @lc code=end

