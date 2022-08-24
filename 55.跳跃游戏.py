#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l==1:
            return True
        dp = nums[0]
        if dp == 0:
            return False
        for i in range(1,l):
            a = max(dp,i+nums[i])
            print(a,i)
            if a >= l-1:
                return True
            if i == a:
                return False
            dp = a
        return True


# @lc code=end

