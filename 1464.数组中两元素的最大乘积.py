#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = 0
        max2 = 0
        for i in range(len(nums)):
            if max1 < nums[i]:
                max2 = max1
                max1 = nums[i]
            elif max2 < nums[i]:
                max2 = nums[i]

        return (max1-1)*(max2-1)



# @lc code=end

