#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#
# 知识点：python深浅拷贝，copy.copy和copy.deepcopy，
# 不考虑空间或者一些重叠更改一般用deepcopy，现在的回溯的写法比较好理解，
# 时间复杂度：O(N*O(卡特兰数))=O(4的N次方/N的二分之一次方)
"""import copy
class Solution:
    def generateChildTrees(self, start, end):
        if start>end:
            return [None]
        if start == end:
            return [TreeNode(start)] 
        return_list = []
        for i in range(start, end+1):
            rightTrees = self.generateChildTrees(start, i-1)
            leftTrees = self.generateChildTrees(i+1,end)
            for rn in rightTrees:
                for ln in leftTrees:
                    root = TreeNode(i, rn, ln)
                    return_list.append(root)
        return return_list
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateChildTrees(1,n)"""
# 更优的办法当然是DP
"""import copy
class Solution:
    def VLR(self, root, i):
        if root:
            root.val+=i
            self.VLR(root.left, i)
            self.VLR(root.right, i)
        else:
            return
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [None]
        dp[1] = [TreeNode(1)]
        for i in range(2,n+1):
            for j in range(1,i+1):
                ln = copy.deepcopy(dp[j-1])
                rn = copy.deepcopy(dp[i-j])
                for l in ln:
                    for r in rn:
                        root = TreeNode(j)
                        root.left = l
                        r1 = copy.deepcopy(r)
                        self.VLR(r1, j)
                        root.right = r1
                        dp[i].append(root)
        return dp[n]
"""

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def generateChildTrees(self, start, end):
        if start>end:
            return [None]
        if start == end:
            return [TreeNode(start)] 
        return_list = []
        for i in range(start, end+1):
            rightTrees = self.generateChildTrees(start, i-1)
            leftTrees = self.generateChildTrees(i+1,end)
            for rn in rightTrees:
                for ln in leftTrees:
                    root = TreeNode(i, rn, ln)
                    return_list.append(root)
        return return_list
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.generateChildTrees(1,n)
        


# @lc code=end

