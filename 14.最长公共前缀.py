#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(200):
            if len(strs[0]) == i:
                return strs[0]
            ch = strs[0][i]
            for str in strs:
                if len(str) == i or str[i] != ch:
                    return str[:i]
        return strs[0]
# @lc code=end

