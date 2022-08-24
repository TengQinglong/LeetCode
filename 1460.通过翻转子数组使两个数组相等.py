#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#
# Counter 是实现的 dict 的一个子类，可以用来方便地计数。
# 详情参考
# https://blog.csdn.net/amq35006/article/details/101255389?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-101255389-blog-114359830.pc_relevant_default&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-101255389-blog-114359830.pc_relevant_default&utm_relevant_index=1

# @lc code=start
from typing import Counter


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        targetset = {}
        for i in target:
            if i in targetset.keys():
                targetset[i]+=1
            else:
                targetset[i]=1
        for j in arr:
            if j not in targetset.keys():
                return False
            else:
                targetset[j]-=1
                if targetset[j] == 0:
                    del targetset[j]
        return True
        return Counter(target) == Counter(arr)

        
# @lc code=end

