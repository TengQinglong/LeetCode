#
# @lc app=leetcode.cn id=2139 lang=python3
#
# [2139] 得到目标值的最少行动次数
#

# @lc code=start
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while(target != 1):
            if target%2==0 :
                if maxDoubles!=0:
                    target/=2
                    count+=1
                    maxDoubles-=1
                else:
                    count+=target-1
                    break
            else:
                target-=1
                count+=1
        return int(count)

# @lc code=end

