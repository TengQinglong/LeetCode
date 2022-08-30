#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#

# @lc code=start


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def f(n):
            if n == 0:
                return 0
            else:
                return n//5+f(n//5)
        if k == 0:
            return 5
        l = k-1
        r = 6*k
        while(l<r):
            m = (r-l)//2 + l
            t = f(m)
            if t == k:
                return 5
            elif t<k:
                l = m+1
            else:
                r = m-1
        return 0
# @lc code=end

