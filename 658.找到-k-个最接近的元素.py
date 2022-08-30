#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr_len = len(arr)
        start_pos = 0
        end_pos = arr_len-1
        ab = [abs(x-n) for n in arr]
        min_arr = 10010
        for i in range(arr_len):
            if ab[i] < min_arr:
                start_pos = i
                min_arr = ab[i]
        if k == 1:
            return [arr[start_pos]]
        end_pos = start_pos+1
        start_pos-=1
        while(end_pos-start_pos<k+1):
            if start_pos < 0:
                return arr[:k]
            if end_pos > arr_len-1:
                return arr[-k:]
            if ab[start_pos]<=ab[end_pos]:
                start_pos-=1
            else:
                end_pos+=1
        return arr[start_pos+1:end_pos]




# @lc code=end

