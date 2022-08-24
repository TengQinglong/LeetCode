#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        nums = []
        T = head
        while(T):
            if left<=count<=right:
                nums.append(T.val)
            T = T.next
            count+=1
        T = head
        count = 1
        while(T):
            if left<=count<=right:
                T.val = nums[-1]
                del nums[-1]
            T = T.next
            count+=1
        return head
            
# @lc code=end

