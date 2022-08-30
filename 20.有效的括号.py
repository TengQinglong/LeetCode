#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack_s = []
        dict = {'(':0,'[':1,'{':2,'}':3,']':4,')':5}
        for i in range(len(s)):
            if len(stack_s):
                if stack_s[-1]+dict[s[i]] == 5 and dict[s[i]]>stack_s[-1]:
                    del stack_s[-1]
                else:
                    stack_s.append(dict[s[i]])
            else:
                stack_s.append(dict[s[i]])
        return True if len(stack_s)==0 else False


# @lc code=end

