#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
# 第一遍想通过广搜做，但是相对距离想通过插入None的方法找，但是会不断插入，遂放弃
# 看了遍题解，第一种思路是跟随结点插入位置

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def nodeDst(l):
            return l[-1][1] - l[0][1] + 1
        max_len = 1
        queue_node = []
        queue_node.append([root,1])
        queue_node.append("#")
        while(len(queue_node) != 1):
            T = queue_node[0][0]
            if T == '#' and len(queue_node):
                del queue_node[0]
                max_len = max(max_len,nodeDst(queue_node))
                queue_node.append("#")
                continue
            if T.left:
                queue_node.append([T.left,2*queue_node[0][1]-1])
            if T.right:
                queue_node.append([T.right,2*queue_node[0][1]])
            del queue_node[0]

        return max_len
            

# @lc code=end

