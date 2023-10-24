class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)-1
        a=0
        b=0
        for i in range(n):
            if nums[i]<=nums[i+1]:
                a+=1
            if nums[i]>=nums[i+1]:
                b+=1
        if a==n or b==n:
            return True
        else:
            return False
#https://leetcode.com/problems/monotonic-array/description/