#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack_num = []
        stack_op = []
        stack_bracket = []
        op_set = ('+','-')
        bracket_set = ('(',')')
        for i in len(len(s)):
            if s[i] in op_set:
                stack_op.append(s[i])
            elif s[i] in bracket_set:
                stack_bracket.append(s[i])
            else:
                
# @lc code=end

