#
# @lc app=leetcode.cn id=1470 lang=python3
#
# [1470] 重新排列数组
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = []
        n = len(nums)//2
        for i in range(n):
            final.append(nums[i])
            final.append(nums[n+i])
        return final
# @lc code=end

