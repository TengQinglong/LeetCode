#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def middlesort(self, root, final):
        if root.left:
            self.middlesort(root.left, final)
        final.append(root.val)
        if root.right:
            self.middlesort(root.right, final)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        if root==None:
            return final
        self.middlesort(root, final)
        return final
        
# @lc code=end

