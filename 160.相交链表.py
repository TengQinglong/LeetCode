#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from code import interact


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA,pB = headA,headB
        flagA, flagB = True, True
        while(pA and pB):
            if pA == pB:
                return pA
            pA=pA.next
            pB=pB.next
            if flagA and pA == None:
                pA = headB
                flagA = False
            if flagB and pB == None:
                pB = headA
                flagB = False
        return None
        

# @lc code=end

