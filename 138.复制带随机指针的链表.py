#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
# 借助哈希表存储原节点与新节点的映射关系
# 时间：O(N) 空间：O(N)
# 也可以原地操作，借助next将新节点插入原节点与下一个原节点中间来节省空间
# 时间:O(N) 空间：O(1)

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        id_map = {}
        new_stack = []
        T = head
        count=0
        while(T):
            id_map[id(T)] = count
            P = Node(T.val,None,T.random)
            new_stack.append(P)
            T = T.next
            count+=1

        for i in range(len(new_stack)):
            if i != len(new_stack)-1:
                new_stack[i].next = new_stack[i+1]
                if new_stack[i].random:
                    pos = id_map[id(new_stack[i].random)]
                    new_stack[i].random = new_stack[pos]
                else:
                    new_stack[i].random = None
            else:
                new_stack[i].next = None
                if new_stack[i].random:
                    pos = id_map[id(new_stack[i].random)]
                    new_stack[i].random = new_stack[pos]
                else:
                    new_stack[i].random = None
        return new_stack[0]
            


            
        
# @lc code=end

