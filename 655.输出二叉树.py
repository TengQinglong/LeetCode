#
# @lc app=leetcode.cn id=655 lang=python3
#
# [655] 输出二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def dfs(root):
            if root == None:
                return 0
            return max(dfs(root.left)+1, dfs(root.right)+1)
        def travel(node, pos, final,height):
            if node:
                final[pos[0]][pos[1]] = str(node.val)
                travel(node.left, [pos[0]+1, pos[1]-(2**(height-pos[0]-2))],final,height)
                travel(node.right, [pos[0]+1, pos[1]+(2**(height-pos[0]-2))],final,height)
            else:
                return
        height = dfs(root)
        n = 2**height-1
        final = [["" for _ in range(n)] for i in range(height)]
        travel(root,[0,(n-1)//2],final,height)
        return final
# @lc code=end

