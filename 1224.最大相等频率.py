#
# @lc app=leetcode.cn id=1224 lang=python3
#
# [1224] 最大相等频率
#

# @lc code=start
class Solution:
    def idenSuffix(self,count_map, freq_map):
        if len(count_map.keys()) == 1:
            return True
        if len(freq_map.keys()) == 1 and list(freq_map.keys())[0] == 1:
            return True
        elif len(freq_map.keys()) == 2 and 1 in freq_map.keys() and freq_map[1] == 1:
            return True
        elif len(freq_map.keys()) == 2 and \
            abs(list(freq_map.keys())[0]-list(freq_map.keys())[1]) == 1 \
                and freq_map[max(list(freq_map.keys()))] == 1:
            return True
        else:
            return False

    def maxEqualFreq(self, nums: List[int]) -> int:
        count_map = {}
        freq_map = {}
        l = len(nums)
        if l<=3:
            return l
        for num in nums:
            if num in count_map.keys():
                count_map[num] += 1
            else:
                count_map[num] = 1
        for value in count_map.values():
            if value in freq_map.keys():
                freq_map[value] += 1
            else:
                freq_map[value] = 1
        print(count_map)
        print(freq_map)
        if self.idenSuffix(count_map, freq_map):
            return l
        for i in range(l-1, 0,-1):
            freq_map[count_map[nums[i]]] -= 1
            if freq_map[count_map[nums[i]]] <= 0:
                del freq_map[count_map[nums[i]]]
            count_map[nums[i]]-=1
            if count_map[nums[i]] == 0:
                del count_map[nums[i]]
            else:    
                if count_map[nums[i]] in freq_map.keys():
                    freq_map[count_map[nums[i]]] +=1 
                else:
                    freq_map[count_map[nums[i]]] = 1
            print(freq_map)
            if self.idenSuffix(count_map, freq_map):
                return i
        return 1

        
                
# @lc code=end

