class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if a or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                a = 1
        return True
#https://leetcode.com/problems/non-decreasing-array/description/