#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        final = [-1,-1]
        if nums == []:
            return final
        head = 0
        tail = len(nums)-1
        while(head<=tail):
            pos = head+(tail-head)//2
            if nums[pos] == target:
                if pos == 0 or nums[pos-1] != target:
                    final[0] = pos
                    break
                else:
                    tail = pos-1
            elif nums[pos] < target:
                head = pos+1
            else:
                tail = pos-1
        else:
            return final
        head = 0
        tail = len(nums)-1
        while(head<=tail):
            pos = head+(tail-head)//2
            if nums[pos] == target:
                if pos == len(nums)-1 or nums[pos+1] != target:
                    final[1] = pos
                    break
                else:
                    head = pos+1
            elif nums[pos] < target:
                head = pos+1
            else:
                tail = pos-1
        return final


# @lc code=end

