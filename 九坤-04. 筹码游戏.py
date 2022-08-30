from functools import lru_cache
class Solution:
    def chipGame(self, nums: List[int], kind: int) -> float:
        # 非升序排列
        nums.sort(reverse=True)
        while len(nums) < kind:
            nums.append(0)
        nums = tuple(nums)
        t = tuple([0] * kind)
        # 深搜本质上是一种模拟
        @lru_cache(None)
        def dfs(t):
            if t == nums:
                return 0
            tl = list(t)
            r = 0
            v = 0
            for i in range(len(tl)):
                tmp = [n for n in tl]
                tmp[i] += 1
                tmp.sort(reverse=True)
                tmp = tuple(tmp)
                if not all(tmp[j] <= nums[j] for j in range(kind)):
                    v += 1 / kind
                    continue
                r += (dfs(tmp) + 1) / kind
            return (v + r) / (1 - v)
        
        return dfs(t)