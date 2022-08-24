#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
# 第一遍用数组做的，单指针每次读到存进去，读下一个对比是否已经进入数组 
# 时间：O(N平方) 空间：O(N)，但是使用python列表的方式内存占用应该是只有地址的？
# 第二遍用快慢指针做 
# 时间：O(N) 空间：O(1)


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                a = head
                b = fast
                while(a!=b):
                    a = a.next
                    b = b.next
                return a
        return None

        
# @lc code=end

