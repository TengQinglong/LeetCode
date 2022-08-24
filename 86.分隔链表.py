#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        stack_small = []
        stack_big = []
        T = head
        if T == None:
            return None
        while(T):
            if T.val < x:
                stack_small.append(T)
            else:
                stack_big.append(T)
            T = T.next        
        if len(stack_small):
            head_new = stack_small[0]
            T = stack_small[0]
            for i in range(1,len(stack_small)):
                T.next = stack_small[i]
                T = stack_small[i]
            T.next=None
        
        if len(stack_big):
            if len(stack_small)==0:
                head_new = stack_big[0]
                T = stack_big[0]
            else:
                T.next = stack_big[0]
                
                T = stack_big[0]
            for j in range(1, len(stack_big)):
                T.next = stack_big[j]
                T = stack_big[j]
            T.next=None
        
        return head_new

# @lc code=end

