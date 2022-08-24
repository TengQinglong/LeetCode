class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        count = 0
        consttemplate =  10**9+7
        nums_len = len(nums)
        for i in range(nums_len):
            nums[i] = nums[i] - int(str(nums[i])[::-1])
            if nums[i] in m.keys():
                m[nums[i]]+=1
            else:
                m[nums[i]]=1
        for i in m.keys():
            count+=m[i]*(m[i]-1)/2
            
        return count%consttemplate