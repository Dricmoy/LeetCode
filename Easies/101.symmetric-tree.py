#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False

            return (tree1.val == tree2.val) and isMirror(tree1.left, tree2.right) and isMirror(tree1.right, tree2.left)
        
        return isMirror(root, root) #check symmetry with itself
        
        
# @lc code=end

