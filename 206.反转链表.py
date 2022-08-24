#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        T = head
        while T:
            stack.append(T.val)
            T = T.next
        T = head
        for i in range(len(stack),0,-1):
            T.val = stack[i-1]
            T = T.next
        return head

# @lc code=end

