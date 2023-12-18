class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        maxV=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
                if maxV<count:
                    maxV=count
            elif nums[i]==nums[i-1]:
                count+=0
            else:
                count=1
        return maxV
        
# https://leetcode.com/problems/longest-consecutive-sequence/submissions/1106584479/