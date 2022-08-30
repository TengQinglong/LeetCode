#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
# 最先的想法是把所有值拿出来排序，把原多个链表连在一起然后遍历一遍挨个赋值，竟然过了
# 时间:O(NlogN) 主要是快排的时间复杂度 空间：O(N) 需要一个额外存储的列表
# 其他解法：
# 1. 逐一合并
# 2. 分治合并
# 3. 一起合并，比较每个头的大小，可以使用优先队列优化

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        condition = lambda t: t != None
        filter_lists = list(filter(condition,lists))
        if len(filter_lists) == 0:
            return None
        if len(filter_lists) == 1:
            return filter_lists[0]

        num_list = []
        for i in range(len(filter_lists)):
            T = filter_lists[i]
            while T:
                num_list.append(T.val)
                if T.next==None:
                    if i != len(filter_lists) - 1:
                        T.next = filter_lists[i+1]
                    T = None
                else:
                    T = T.next
        num_list.sort()

        T = filter_lists[0]
        while T:
            T.val = num_list[0]
            del num_list[0]
            T = T.next
        return filter_lists[0]

# @lc code=end

